import re

filename = "tfb.html"

with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

# Add style for yellow headers
style_addition = '''<link rel="stylesheet" href="css/style.css" />
  <style>
    h1, h2, h3, h4, h5, h6 {
      color: #FFC000 !important;
    }
  </style>'''
content = content.replace('<link rel="stylesheet" href="css/style.css" />', style_addition)

# Add logo div inside <main class="container">
logo_div = '''<main class="container">
    <div style="text-align: left; margin-bottom: 30px;">
        <img src="data/logo-sello-universitat-carlemany.png.webp" alt="Logo Universitat Carlemany" width="150" />
    </div>'''
content = content.replace('<main class="container">', logo_div)

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated logo and header colors in tfb.html")
