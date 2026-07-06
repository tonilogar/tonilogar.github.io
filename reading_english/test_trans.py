import urllib.request, json, urllib.parse

words = [
    'selfish', 'detachment', 'to rot', 'grounded', 'to melt', 
    'oppressive', 'shatter', 'burden', 'I just need one day of peace', 
    'He wanted to use time travel to meet Siddhartha Gautama'
]

for w in words:
    url = f'https://api.mymemory.translated.net/get?q={urllib.parse.quote(w)}&langpair=en|es'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            print(f"EN: {w}")
            print(f"ES: {data['responseData']['translatedText']}")
            print("-" * 30)
    except Exception as e:
        print(f'Error for {w}: {e}')
