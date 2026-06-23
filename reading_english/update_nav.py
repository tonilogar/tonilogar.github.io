import os

css_content = """
/* --- Story Navigation --- */
.story-navigation {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(255,255,255,0.05);
    flex-wrap: wrap;
}

.nav-btn {
    padding: 0.75rem 1.5rem;
    background-color: var(--primary-color);
    color: white;
    text-decoration: none;
    border-radius: 0.5rem;
    font-weight: 600;
    text-align: center;
    transition: background-color 0.3s ease;
    flex: 1;
    min-width: 150px;
}

.nav-btn:hover {
    background-color: #2563eb;
}

.nav-btn.secondary {
    background-color: #334155;
}

.nav-btn.secondary:hover {
    background-color: #475569;
}
"""

with open("css/story.css", "a", encoding="utf-8") as f:
    f.write(css_content)

stories = [
    "the_lost_key.html",
    "the_great_campout.html",
    "the_mystery_box.html",
    "next_summer.html",
    "the_animal_race.html",
    "the_lost_boarding_pass.html",
    "the_first_day_of_class.html",
    "gaudi_mystery_part1.html",
    "something_brutal.html",
    "the_blackout.html"
]

for i, story in enumerate(stories):
    next_story = stories[i+1] if i + 1 < len(stories) else "index.html"
    next_text = "Next Story ➡" if i + 1 < len(stories) else "Back to Index ➡"
    
    nav_html = f"""
        <div class="story-navigation">
            <a href="index.html" class="nav-btn secondary">⬅ All Stories</a>
            <a href="my_vocabulary.html" class="nav-btn secondary">📖 My Vocabulary</a>
            <a href="{next_story}" class="nav-btn">{next_text}</a>
        </div>
    </main>"""
    
    with open(story, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "class=\"story-navigation\"" not in content:
        content = content.replace("</main>", nav_html)
        with open(story, "w", encoding="utf-8") as f:
            f.write(content)

print("Updated all stories and CSS.")
