const VIEWS = [
    "homeView",
    "welcomeView",
    "contentView",
    "registeredView",
    "notRegisteredView",
];

let currentName = "";

function $(selector) {
    return document.querySelector(selector);
}

function showView(id) {
    VIEWS.forEach((viewId) => {
        const view = document.getElementById(viewId);
        if (view) {
            view.classList.toggle("active", viewId === id);
        }
    });
}

function showFeedback(message, isError = false) {
    const feedback = $("#feedback");
    if (!feedback) return;
    feedback.textContent = message;
    feedback.style.background = isError ? "#dc2626" : "#111827";
    feedback.classList.add("visible");
    setTimeout(() => feedback.classList.remove("visible"), 2400);
}

async function registerName(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const input = $("#nombre");
    const name = input.value.trim();

    if (!name) {
        showFeedback("Introduce un nombre válido.", true);
        return;
    }

    form.querySelector("button").disabled = true;
    try {
        const { error } = await supabaseClient.from("user_names").insert({ name });
        if (error) {
            console.error(error);
            showFeedback("No se pudo guardar el nombre.", true);
            return;
        }
        currentName = name;
        $("#welcomeName").textContent = currentName;
        input.value = "";
        showView("welcomeView");
        showFeedback("Nombre guardado correctamente.");
    } finally {
        form.querySelector("button").disabled = false;
    }
}

async function verifyName(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const input = $("#verificacion");
    const name = input.value.trim();

    if (!name) {
        showFeedback("Introduce un nombre para verificar.", true);
        return;
    }

    form.querySelector("button").disabled = true;
    try {
        const { data, error } = await supabaseClient
            .from("user_names")
            .select("id")
            .eq("name", name)
            .maybeSingle();
        if (error && error.code !== "PGRST116") {
            console.error(error);
            showFeedback("No se pudo comprobar el nombre.", true);
            return;
        }
        if (data) {
            $("#registeredName").textContent = name;
            showView("registeredView");
        } else {
            $("#notRegisteredName").textContent = name;
            showView("notRegisteredView");
        }
    } finally {
        form.querySelector("button").disabled = false;
    }
}

function setupNavigation() {
    $("#goToContent").addEventListener("click", () => showView("contentView"));
    $("#welcomeToContent").addEventListener("click", () => showView("contentView"));
    $("#backToHome").addEventListener("click", () => showView("homeView"));
    $("#contentBackHome").addEventListener("click", () => showView("homeView"));
    $("#registeredToContent").addEventListener("click", () => showView("contentView"));
    $("#registeredToHome").addEventListener("click", () => showView("homeView"));
    $("#notRegisteredToHome").addEventListener("click", () => showView("homeView"));
    $("#notRegisteredToContent").addEventListener("click", () => showView("contentView"));
}

document.addEventListener("DOMContentLoaded", () => {
    if (!supabaseClient) {
        showFeedback("Configura Supabase correctamente.", true);
        return;
    }
    $("#registerForm").addEventListener("submit", registerName);
    $("#verifyForm").addEventListener("submit", verifyName);
    setupNavigation();
});
