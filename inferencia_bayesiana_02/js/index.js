function toggleIndice() {
  var lista = document.getElementById("listaEjercicios");
  if (lista.style.display === "none" || lista.style.display === "") {
    lista.style.display = "block";
  } else {
    lista.style.display = "none";
  }
}
