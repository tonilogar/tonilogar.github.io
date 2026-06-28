import re

filename = "tfb_001.md"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

logo_html = '''<div style="text-align: left; margin-bottom: 30px;">
    <img src="../data/logo-sello-universitat-carlemany.png.webp" alt="Logo Universitat Carlemany" width="150" />
</div>\n\n'''

new_lines = []
for i, line in enumerate(lines):
    if i == 0 and line.startswith("# "):
        new_lines.append(logo_html)
        match = re.match(r"^# (.*)", line)
        if match:
            new_lines.append(f'# <span style="color: #FFC000;">{match.group(1).strip()}</span>\n')
        else:
            new_lines.append(line)
    elif line.startswith("## "):
        match = re.match(r"^## (.*)", line)
        if match:
            new_lines.append(f'## <span style="color: #FFC000;">{match.group(1).strip()}</span>\n')
        else:
            new_lines.append(line)
    elif line.startswith("### "):
        match = re.match(r"^### (.*)", line)
        if match:
            new_lines.append(f'### <span style="color: #FFC000;">{match.group(1).strip()}</span>\n')
        else:
            new_lines.append(line)
    elif line.startswith("#### "):
        match = re.match(r"^#### (.*)", line)
        if match:
            new_lines.append(f'#### <span style="color: #FFC000;">{match.group(1).strip()}</span>\n')
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open(filename, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Updated logo and header colors in", filename)
