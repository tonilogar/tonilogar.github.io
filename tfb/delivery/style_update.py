import re
import sys

filename = "propuesta_entrega_005.md"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if i == 0 and line.startswith("# Propuesta"):
        new_lines.append('<div style="text-align: center; margin-bottom: 30px;">\n')
        new_lines.append('    <img src="../data/logo-sello-universitat-carlemany.png.webp" alt="Logo Universitat Carlemany" width="250" />\n')
        new_lines.append('</div>\n\n')
        new_lines.append('# <span style="color: #004b87;">Propuesta del Trabajo Final de Bàtxelor (TFB)</span>\n')
    elif line.startswith("## "):
        match = re.match(r"## (.*)", line)
        if match:
            text = match.group(1).strip()
            new_lines.append(f'## <span style="color: #004b87;">{text}</span>\n')
        else:
            new_lines.append(line)
    elif line.startswith("### "):
        match = re.match(r"### (.*)", line)
        if match:
            text = match.group(1).strip()
            new_lines.append(f'### <span style="color: #004b87;">{text}</span>\n')
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open(filename, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Done updating styles in", filename)
