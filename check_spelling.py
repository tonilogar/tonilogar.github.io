import win32com.client
import sys
import os

word = win32com.client.DispatchEx('Word.Application')
word.Visible = False

try:
    doc_path = r'\\wsl.localhost\Ubuntu\home\tonilogar\trabajos\programming\tonilogar.github.io\tfb\delivery\entrega_deposito_final_primera_defensa_antonio_lopez.docx'
    
    # Just to be safe with Protected View, copy it locally
    import shutil
    local_path = r'C:\Users\a.lopez.g\.gemini\antigravity-ide\brain\ff3157d4-bc22-4220-8f48-a4774f373c38\scratch\temp_spell.docx'
    shutil.copy2(doc_path, local_path)
    
    doc = word.Documents.Open(local_path)
    
    errors = doc.SpellingErrors
    error_list = []
    
    for err in errors:
        error_list.append(err.Text)
        
    doc.Close(False)
    
    # Count frequencies
    from collections import Counter
    counts = Counter(error_list)
    print("Spelling errors found (Top 50):")
    for word, count in counts.most_common(50):
        print(f"{word}: {count}")
        
except Exception as e:
    print(f"Error: {e}")
finally:
    word.Quit()
