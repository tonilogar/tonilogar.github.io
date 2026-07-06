import os

fixes = {
    "generate_genesis_p4.py": ("""<a href="index.html" class="nav-btn">Back to Index ➡</a>""", """<a href="the_chronos_protocol_part4.html" class="nav-btn">Next Story ➡</a>"""),
    "the_chronos_genesis_part4.html": ("""<a href="index.html" class="nav-btn">Back to Index ➡</a>""", """<a href="the_chronos_protocol_part4.html" class="nav-btn">Next Story ➡</a>"""),
    
    "generate_protocol_p4.py": ("""<a href="index.html" class="nav-btn">Back to Index ➡</a>""", """<a href="the_chronos_rebellion_part1.html" class="nav-btn">Next Story ➡</a>"""),
    "the_chronos_protocol_part4.html": ("""<a href="index.html" class="nav-btn">Back to Index ➡</a>""", """<a href="the_chronos_rebellion_part1.html" class="nav-btn">Next Story ➡</a>"""),
    
    "generate_rebellion_p1.py": ("""<a href="index.html" class="nav-btn">Next Story ➡</a>""", """<a href="the_chronos_rebellion_part2.html" class="nav-btn">Next Story ➡</a>"""),
    "the_chronos_rebellion_part1.html": ("""<a href="index.html" class="nav-btn">Next Story ➡</a>""", """<a href="the_chronos_rebellion_part2.html" class="nav-btn">Next Story ➡</a>"""),
    
    "generate_rebellion_p2.py": ("""<a href="index.html" class="nav-btn">Next Story ➡</a>""", """<a href="the_chronos_rebellion_part3.html" class="nav-btn">Next Story ➡</a>"""),
    "the_chronos_rebellion_part2.html": ("""<a href="index.html" class="nav-btn">Next Story ➡</a>""", """<a href="the_chronos_rebellion_part3.html" class="nav-btn">Next Story ➡</a>"""),
    
    "generate_rebellion_p3.py": ("""<a href="index.html" class="nav-btn">Next Story ➡</a>""", """<a href="the_chronos_rebellion_part4.html" class="nav-btn">Next Story ➡</a>"""),
    "the_chronos_rebellion_part3.html": ("""<a href="index.html" class="nav-btn">Next Story ➡</a>""", """<a href="the_chronos_rebellion_part4.html" class="nav-btn">Next Story ➡</a>"""),
    
    "generate_rebellion_p4.py": ("""<a href="index.html" class="nav-btn">Next Story ➡</a>""", """<a href="the_chronos_rebellion_part5.html" class="nav-btn">Next Story ➡</a>"""),
    "the_chronos_rebellion_part4.html": ("""<a href="index.html" class="nav-btn">Next Story ➡</a>""", """<a href="the_chronos_rebellion_part5.html" class="nav-btn">Next Story ➡</a>"""),
    
    "generate_rebellion_p5.py": ("""<a href="index.html" class="nav-btn">Back to Index ➡</a>""", """<a href="the_chronos_rebellion_part6.html" class="nav-btn">Next Story ➡</a>"""),
    "the_chronos_rebellion_part5.html": ("""<a href="index.html" class="nav-btn">Back to Index ➡</a>""", """<a href="the_chronos_rebellion_part6.html" class="nav-btn">Next Story ➡</a>"""),
    
    "generate_rebellion_p6.py": ("""<a href="index.html" class="nav-btn">Back to Index ➡</a>""", """<a href="the_chronos_rebellion_part7.html" class="nav-btn">Next Story ➡</a>"""),
    "the_chronos_rebellion_part6.html": ("""<a href="index.html" class="nav-btn">Back to Index ➡</a>""", """<a href="the_chronos_rebellion_part7.html" class="nav-btn">Next Story ➡</a>"""),
}

for filename, (old_str, new_str) in fixes.items():
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        if old_str in content:
            content = content.replace(old_str, new_str)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed {filename}")
        else:
            print(f"Could not find old string in {filename}")
    else:
        print(f"File {filename} does not exist")
