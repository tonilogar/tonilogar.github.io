import re

filename = "propuesta_entrega_005.md"

with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the logo div alignment and width
old_logo_div = '''<div style="text-align: center; margin-bottom: 30px;">
    <img src="../data/logo-sello-universitat-carlemany.png.webp" alt="Logo Universitat Carlemany" width="250" />
</div>'''

new_logo_div = '''<div style="text-align: left; margin-bottom: 20px;">
    <img src="../data/logo-sello-universitat-carlemany.png.webp" alt="Logo Universitat Carlemany" width="150" />
</div>'''

content = content.replace(old_logo_div, new_logo_div)

# Replace the color of the headings to yellow
content = content.replace('color: #004b87;', 'color: #FFC000;')

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated logo alignment to left and heading colors to yellow.")
