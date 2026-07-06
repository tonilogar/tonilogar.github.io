import os
import glob

# 1. Update translator.js
js_path = "js/translator.js"
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

old_fetch = """            const res = await fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=en|es`);
            const data = await res.json();
            
            if (data && data.responseData && data.responseData.translatedText) {
                const translation = data.responseData.translatedText;"""

new_fetch = """            let translation = null;

            // 1. Smart Dictionary (Story Context)
            if (window.currentStoryVocabulary) {
                const found = window.currentStoryVocabulary.find(v => v.en.toLowerCase() === text.toLowerCase());
                if (found) {
                    translation = found.es;
                }
            }

            // 2. Fallback to Google Translate Free API
            if (!translation) {
                const res = await fetch(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=es&dt=t&q=${encodeURIComponent(text)}`);
                const data = await res.json();
                if (data && data[0] && data[0][0] && data[0][0][0]) {
                    translation = data[0][0][0];
                }
            }
            
            if (translation) {"""

if old_fetch in js_content:
    js_content = js_content.replace(old_fetch, new_fetch)
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Updated translator.js")
else:
    print("Could not find fetch block in translator.js. Already updated?")


# 2. Update all .py and .html files to expose storyVocabulary
old_init = "initMatchingGame('pre-vocab', storyVocabulary);"
new_init = "window.currentStoryVocabulary = storyVocabulary;\n            initMatchingGame('pre-vocab', storyVocabulary);"

files_to_check = glob.glob("*.py") + glob.glob("*.html")
updated_count = 0

for file_path in files_to_check:
    if file_path == os.path.basename(__file__):
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if old_init in content and "window.currentStoryVocabulary =" not in content:
        content = content.replace(old_init, new_init)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1
        print(f"Updated {file_path}")

print(f"Finished updating {updated_count} files.")
