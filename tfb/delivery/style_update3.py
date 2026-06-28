import re

filename = "propuesta_entrega_005.md"

with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

old_logo_div = '''<div style="text-align: left; margin-bottom: 20px;">
    <img src="../data/logo-sello-universitat-carlemany.png.webp" alt="Logo Universitat Carlemany" width="150" />
</div>'''

new_logo_div = '''<style>
  /* Estilos para repetir el logo en cada página al imprimir o exportar a PDF */
  @media print {
    .doc-header {
      position: fixed;
      top: 0;
      left: 0;
    }
    body {
      padding-top: 80px;
    }
  }
</style>
<div class="doc-header" style="text-align: left; margin-bottom: 20px;">
    <img src="../data/logo-sello-universitat-carlemany.png.webp" alt="Logo Universitat Carlemany" width="150" />
</div>'''

content = content.replace(old_logo_div, new_logo_div)

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated logo div to include repeating print header.")
