import os
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Update numbers in B1 stories
content = content.replace("5. The Lost Boarding Pass", "6. The Lost Boarding Pass")
content = content.replace("6. The First Day of Class", "7. The First Day of Class")
content = content.replace("7. The Gaudí Mystery: Part 1", "8. The Gaudí Mystery: Part 1")
content = content.replace("8. Something Brutal", "9. Something Brutal")
content = content.replace("9. The Blackout", "10. The Blackout")

new_story_html = """
                <a href="the_chronos_protocol_part1.html" class="story-item" style="border-left: 4px solid #ef4444;">
                    <div class="story-info">
                        <h3 style="color: #ef4444;">5. The Chronos Protocol: Part 1</h3>
                        <div class="story-path">Nivel A2+ Mega-Story • Vocabulario: Misterio Sci-Fi • Gramática: Pasado Simple & Superlativos</div>
                    </div>
                    <div class="story-arrow" style="color: #ef4444;">&rarr;</div>
                </a>

                <a href="the_lost_boarding_pass.html" class="story-item" style="border-left: 4px solid #c084fc;">"""

content = content.replace('<a href="the_lost_boarding_pass.html" class="story-item" style="border-left: 4px solid #c084fc;">', new_story_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

# Fix next story link in the_animal_race.html
with open("the_animal_race.html", "r", encoding="utf-8") as f:
    animal_content = f.read()

animal_content = animal_content.replace('href="the_lost_boarding_pass.html" class="nav-btn">Next Story', 'href="the_chronos_protocol_part1.html" class="nav-btn">Next Story')

with open("the_animal_race.html", "w", encoding="utf-8") as f:
    f.write(animal_content)

print("Updated index.html and the_animal_race.html")
