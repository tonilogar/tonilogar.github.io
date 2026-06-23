import os

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Update numbers in B1 stories
content = content.replace("6. The Lost Boarding Pass", "8. The Lost Boarding Pass")
content = content.replace("7. The First Day of Class", "9. The First Day of Class")
content = content.replace("8. The Gaudí Mystery: Part 1", "10. The Gaudí Mystery: Part 1")
content = content.replace("9. Something Brutal", "11. Something Brutal")
content = content.replace("10. The Blackout", "12. The Blackout")

new_story_html = """
                <a href="the_chronos_protocol_part1.html" class="story-item" style="border-left: 4px solid #ef4444;">
                    <div class="story-info">
                        <h3 style="color: #ef4444;">5. The Chronos Protocol: Part 1</h3>
                        <div class="story-path">Nivel A2+ Mega-Story • Vocabulario: Misterio Sci-Fi • Gramática: Pasado Simple & Superlativos</div>
                    </div>
                    <div class="story-arrow" style="color: #ef4444;">&rarr;</div>
                </a>

                <a href="the_chronos_protocol_part2.html" class="story-item" style="border-left: 4px solid #ef4444;">
                    <div class="story-info">
                        <h3 style="color: #ef4444;">6. The Chronos Protocol: Part 2</h3>
                        <div class="story-path">Nivel A2+ Mega-Story • Vocabulario: Peligro y Mar • Gramática: Past Continuous & Prepositions</div>
                    </div>
                    <div class="story-arrow" style="color: #ef4444;">&rarr;</div>
                </a>

                <a href="the_chronos_protocol_part3.html" class="story-item" style="border-left: 4px solid #ef4444;">
                    <div class="story-info">
                        <h3 style="color: #ef4444;">7. The Chronos Protocol: Part 3</h3>
                        <div class="story-path">Nivel A2+ Mega-Story • Vocabulario: Tiempo y Combate • Gramática: Future & Conditionals</div>
                    </div>
                    <div class="story-arrow" style="color: #ef4444;">&rarr;</div>
                </a>

                <a href="the_lost_boarding_pass.html" class="story-item" style="border-left: 4px solid #c084fc;">"""

# We need to replace the block starting from the Part 1 link up to the boarding pass link.
# We'll just replace the Part 1 block and the boarding pass opening tag with our new combined block.
old_block = """
                <a href="the_chronos_protocol_part1.html" class="story-item" style="border-left: 4px solid #ef4444;">
                    <div class="story-info">
                        <h3 style="color: #ef4444;">5. The Chronos Protocol: Part 1</h3>
                        <div class="story-path">Nivel A2+ Mega-Story • Vocabulario: Misterio Sci-Fi • Gramática: Pasado Simple & Superlativos</div>
                    </div>
                    <div class="story-arrow" style="color: #ef4444;">&rarr;</div>
                </a>

                <a href="the_lost_boarding_pass.html" class="story-item" style="border-left: 4px solid #c084fc;">"""

content = content.replace(old_block, new_story_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html")
