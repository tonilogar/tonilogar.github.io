import zipfile
import xml.etree.ElementTree as ET
import sys

def read_docx(path):
    with zipfile.ZipFile(path) as docx:
        xml_content = docx.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    text = []
    for p in tree.iterfind('.//w:p', namespace):
        texts = [node.text for node in p.iterfind('.//w:t', namespace) if node.text]
        if texts:
            text.append(''.join(texts))
    return '\n'.join(text)

if len(sys.argv) > 1:
    print(f"--- {sys.argv[1]} ---")
    print(read_docx(sys.argv[1]))
