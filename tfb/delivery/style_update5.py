import re

filename = "propuesta_entrega_005.md"

with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

old_logo_div = '''<style>
  /* Fix para que el logo no pise el texto en la exportación */
  @media print {
    .doc-header {
      position: fixed;
      top: 0;
      left: 0;
      background-color: white;
      width: 100%;
      padding-bottom: 10px;
      z-index: 1000;
    }
    @page {
      margin-top: 120px;
    }
    body {
      margin-top: 100px;
    }
  }
</style>
<div class="doc-header" style="text-align: left; margin-bottom: 60px; display: block; height: auto;">
    <img src="../data/logo-sello-universitat-carlemany.png.webp" alt="Logo Universitat Carlemany" width="150" style="background-color: white;" />
</div>
<br>'''

new_logo_div = '''<div style="text-align: left; margin-bottom: 30px;">
    <img src="../data/logo-sello-universitat-carlemany.png.webp" alt="Logo Universitat Carlemany" width="150" />
</div>'''

content = content.replace(old_logo_div, new_logo_div)

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print("Reverted to simple top-left logo.")
