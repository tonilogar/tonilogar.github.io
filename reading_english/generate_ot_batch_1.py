import os

stories = [
    {
        "filename": "ot_01_creation.html",
        "title": "The Creation and the Garden of Eden",
        "level": "Nivel B2",
        "focus": "Vocabulario: Creación y Naturaleza • Gramática: Passive Voice",
        "h2_title": "The Beginning of Everything",
        "text": """
            <p>In the beginning, the universe was entirely dark and empty. There was no sound, no light, and no life. Then, God spoke, and light was created. The darkness was separated from the light, creating the first day and night.</p>

            <p>Over the next few days, the world was carefully designed. The sky was formed to separate the waters, and dry land was gathered together. Soon, the earth was covered with lush green plants, tall trees, and colorful flowers. The sun, moon, and stars were placed in the sky to mark the seasons and illuminate the world.</p>

            <p>Then, the oceans were filled with swimming creatures, and the sky was filled with flying birds. The land was populated with wild animals of every shape and size. Finally, God created humanity. The first man, Adam, was formed from the dust of the ground, and the breath of life was breathed into him. Later, the first woman, Eve, was created to be his partner.</p>

            <p>Adam and Eve were placed in a magnificent paradise called the Garden of Eden. They were given permission to eat from any tree in the garden, except one: the Tree of the Knowledge of Good and Evil. They were warned that if they ate its fruit, they would certainly die.</p>

            <p>Life in the garden was peaceful until a cunning serpent approached Eve. "Did God really say you must not eat from any tree?" the serpent asked deceptively. He convinced her that the fruit would make her as wise as God. Tempted by the beautiful fruit and the promise of wisdom, Eve ate it and gave some to Adam, who also ate.</p>

            <p>Suddenly, their innocence was lost. They realized they were naked and hid from God out of shame. Because the one rule of the garden had been broken, they were expelled from Eden forever. An angel with a flaming sword was placed at the entrance to ensure they could never return.</p>
        """,
        "quiz": [
            ("What was created on the first day?", "The sun and moon", "Light", "Animals", 1),
            ("From what was the first man formed?", "From water", "From a tree", "From the dust of the ground", 2),
            ("Which tree were they forbidden to eat from?", "The Tree of Life", "The Tree of the Knowledge of Good and Evil", "The Apple Tree", 1),
            ("Why were they expelled from the garden?", "Because they broke the only rule", "Because the garden was too small", "Because they wanted to leave", 0)
        ],
        "vocab": [
            {'id': '1', 'en': 'to design', 'es': 'diseñar'},
            {'id': '2', 'en': 'lush', 'es': 'exuberante'},
            {'id': '3', 'en': 'to populate', 'es': 'poblar'},
            {'id': '4', 'en': 'dust', 'es': 'polvo'},
            {'id': '5', 'en': 'forbidden', 'es': 'prohibido'},
            {'id': '6', 'en': 'cunning', 'es': 'astuto'},
            {'id': '7', 'en': 'innocence', 'es': 'inocencia'},
            {'id': '8', 'en': 'to expel', 'es': 'expulsar'}
        ]
    },
    {
        "filename": "ot_02_cain_abel.html",
        "title": "Cain and Abel",
        "level": "Nivel B2",
        "focus": "Vocabulario: Familia y Celos • Gramática: Past Perfect",
        "h2_title": "The First Brothers",
        "text": """
            <p>After Adam and Eve had been expelled from the Garden of Eden, they started a new life in a harsh world. They had two sons: Cain, who worked the soil as a farmer, and Abel, who kept flocks as a shepherd.</p>

            <p>Time passed, and the day came for the brothers to present an offering to the Lord. Cain brought some of the fruits of the soil he had grown. Abel, however, brought the best portions of the firstborn lambs from his flock. The Lord looked with favor on Abel and his offering, because Abel had given his absolute best with a pure heart.</p>

            <p>But the Lord did not look with favor on Cain's offering. Cain became furious, and his face was downcast. God asked him, "Why are you angry? If you do what is right, will you not be accepted? But if you do not do what is right, sin is crouching at your door; it desires to have you, but you must rule over it."</p>

            <p>Despite the warning, Cain had already let jealousy poison his mind. He had convinced himself that his brother was an enemy. One day, Cain said to his brother, "Let's go out to the field." While they were in the field, Cain attacked his brother Abel and killed him.</p>

            <p>Later, the Lord asked Cain, "Where is your brother Abel?"</p>
            
            <p>"I don't know," he replied defensively. "Am I my brother's keeper?"</p>

            <p>God already knew what had happened. He said, "What have you done? Listen! Your brother's blood cries out to me from the ground." Because Cain had committed this terrible crime, God cursed him. He would wander the earth as a restless fugitive, and the ground would no longer yield crops for him.</p>

            <p>Although Cain had committed murder, God showed him a sliver of mercy. He put a mark on Cain so that no one who found him would kill him. Cain left the presence of the Lord and lived in the land of Nod, forever carrying the weight of his actions.</p>
        """,
        "quiz": [
            ("What were the professions of the two brothers?", "Both were farmers", "Cain was a farmer, Abel was a shepherd", "Cain was a shepherd, Abel was a farmer", 1),
            ("Why was God pleased with Abel's offering?", "Because God prefers meat over vegetables", "Because Abel gave the best he had with a pure heart", "Because Abel brought a lot of food", 1),
            ("What emotion consumed Cain?", "Jealousy", "Fear", "Sadness", 0),
            ("What was Cain's punishment?", "He was sent back to Eden", "He became a wandering fugitive", "He had to work as a shepherd", 1)
        ],
        "vocab": [
            {'id': '1', 'en': 'harsh', 'es': 'duro / severo'},
            {'id': '2', 'en': 'flock', 'es': 'rebaño'},
            {'id': '3', 'en': 'offering', 'es': 'ofrenda'},
            {'id': '4', 'en': 'furious', 'es': 'furioso'},
            {'id': '5', 'en': 'jealousy', 'es': 'celos'},
            {'id': '6', 'en': 'to wander', 'es': 'vagar'},
            {'id': '7', 'en': 'fugitive', 'es': 'fugitivo'},
            {'id': '8', 'en': 'mercy', 'es': 'misericordia'}
        ]
    },
    {
        "filename": "ot_03_noah.html",
        "title": "Noah's Ark and the Great Flood",
        "level": "Nivel B2",
        "focus": "Vocabulario: Clima y Supervivencia • Gramática: Reported Speech",
        "h2_title": "The Great Rain",
        "text": """
            <p>Generations after the first humans, the world had become full of corruption and violence. God saw how wicked the human race had become and regretted having made them. He decided to send a devastating flood to wipe out everything on the earth. However, there was one righteous man who still found favor in God's eyes: Noah.</p>

            <p>God commanded Noah to build a massive wooden ark. He explained that a flood was coming and told Noah that he must bring his family inside to survive. God also instructed him to bring two of all living creatures, male and female, along with enough food for everyone.</p>

            <p>The neighbors laughed at Noah. They told him that he was crazy and that it was never going to rain that much. But Noah ignored them. He said that he was following God's instructions. It took many years, but Noah and his sons eventually finished the colossal ship.</p>

            <p>When the ark was ready, Noah, his family, and the animals went inside, and God shut the door. Seven days later, the sky turned completely black. The springs of the great deep burst forth, and the floodgates of the heavens were opened. It rained endlessly for forty days and forty nights.</p>

            <p>The waters rose higher and higher, eventually covering even the tallest mountains. Every living thing on the dry land perished, but the ark floated safely on the surface of the raging waters. Noah's family and the animals were secure inside, just as God had promised.</p>

            <p>Months later, the rain stopped, and the waters slowly began to recede. The ark came to rest on the mountains of Ararat. Noah sent out a dove, and when it returned with a fresh olive leaf in its beak, he knew the earth was finally drying. When they stepped out of the ark, they saw a brilliant rainbow across the sky. God promised that He would never again destroy the earth with a flood, and the rainbow would be the eternal sign of that covenant.</p>
        """,
        "quiz": [
            ("Why did God decide to flood the earth?", "Because it was too hot", "Because humans had become violent and wicked", "Because He wanted to make new animals", 1),
            ("What did Noah's neighbors think of him?", "They thought he was a genius", "They thought he was crazy", "They helped him build the ark", 1),
            ("How long did it rain?", "For a week", "For a year", "For forty days and forty nights", 2),
            ("What did the rainbow symbolize?", "The end of winter", "A promise never to flood the earth again", "A path to heaven", 1)
        ],
        "vocab": [
            {'id': '1', 'en': 'wicked', 'es': 'malvado'},
            {'id': '2', 'en': 'righteous', 'es': 'justo'},
            {'id': '3', 'en': 'ark', 'es': 'arca'},
            {'id': '4', 'en': 'to perish', 'es': 'perecer'},
            {'id': '5', 'en': 'to recede', 'es': 'retroceder / disminuir'},
            {'id': '6', 'en': 'dove', 'es': 'paloma'},
            {'id': '7', 'en': 'rainbow', 'es': 'arcoíris'},
            {'id': '8', 'en': 'covenant', 'es': 'pacto'}
        ]
    },
    {
        "filename": "ot_04_babel.html",
        "title": "The Tower of Babel",
        "level": "Nivel B2",
        "focus": "Vocabulario: Construcción y Ambición • Gramática: Purpose Clauses",
        "h2_title": "The City in the Clouds",
        "text": """
            <p>Many years after the Great Flood, the descendants of Noah multiplied and spread out. At that time, the whole world had only one language and a common speech. As people moved eastward, they found a wide plain in the land of Shinar and decided to settle there.</p>

            <p>The people became highly ambitious. They said to each other, "Come, let's make bricks and bake them thoroughly so that we can build a great city for ourselves." They wanted to construct a massive tower that would reach to the heavens in order to make a name for themselves and avoid being scattered over the face of the whole earth.</p>

            <p>Driven by pride, they worked tirelessly. They used brick instead of stone, and tar for mortar. The tower grew taller every day, becoming a monument to human arrogance. They believed they didn't need God, thinking they could achieve divinity through their own engineering.</p>

            <p>But the Lord came down to see the city and the tower the people were building. He observed their arrogance and realized that, since they spoke the same language, this was only the beginning of what they would try to do. Nothing they planned would be impossible for them if their pride was left unchecked.</p>

            <p>To stop their arrogant rebellion, God said, "Let us go down and confuse their language so they will not understand each other." Suddenly, the workers could no longer communicate. A request for a brick was answered with a bucket of water. Confusion spread rapidly across the construction site.</p>

            <p>Unable to understand one another, they were forced to stop building the city. Frustrated and divided, the people scattered from there over all the earth, just as they had originally feared. The abandoned city was called Babel, because it was there that the Lord confused the language of the whole world.</p>
        """,
        "quiz": [
            ("What did all people share at the beginning of the story?", "The same religion", "One common language", "The same king", 1),
            ("Why did the people want to build the tower?", "To make a name for themselves and reach the heavens", "To escape another flood", "To communicate with aliens", 0),
            ("What material did they use for construction?", "Wood and nails", "Stone and mud", "Bricks and tar", 2),
            ("How did God stop the construction?", "He sent a thunderstorm", "He confused their language", "He destroyed the tower with an earthquake", 1)
        ],
        "vocab": [
            {'id': '1', 'en': 'descendants', 'es': 'descendientes'},
            {'id': '2', 'en': 'ambitious', 'es': 'ambicioso'},
            {'id': '3', 'en': 'brick', 'es': 'ladrillo'},
            {'id': '4', 'en': 'tar', 'es': 'alquitrán'},
            {'id': '5', 'en': 'arrogance', 'es': 'arrogancia'},
            {'id': '6', 'en': 'rebellion', 'es': 'rebelión'},
            {'id': '7', 'en': 'to confuse', 'es': 'confundir'},
            {'id': '8', 'en': 'scattered', 'es': 'disperso'}
        ]
    }
]

def generate_html(story):
    quiz_html = ""
    for i, q in enumerate(story['quiz']):
        quiz_html += f'''
            <div class="quiz-question">
                <p>{i+1}. {q[0]}</p>
                <button class="quiz-btn" onclick="checkAnswer(this, {str(q[4]==0).lower()})">{q[1]}</button>
                <button class="quiz-btn" onclick="checkAnswer(this, {str(q[4]==1).lower()})">{q[2]}</button>
                <button class="quiz-btn" onclick="checkAnswer(this, {str(q[4]==2).lower()})">{q[3]}</button>
            </div>'''

    vocab_json = str(story['vocab']).replace("'", '"')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reading English - {story['title']}">
    <title>{story['title']} - Reading English</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/story.css">
</head>
<body>
    <header class="main-header story-header">
        <nav class="navbar">
            <div class="logo">Reading English</div>
            <ul class="nav-links">
                <li><a href="index.html">Stories</a></li>
                <li><a href="my_vocabulary.html">My Vocabulary</a></li>
            </ul>
        </nav>
        <div class="hero story-hero" style="background: linear-gradient(135deg, #b45309, #d97706);">
            <h1>{story['title']}</h1>
            <p>Level: B2 | Focus: {story['focus']}</p>
        </div>
    </header>

    <main class="content story-content">
        <section class="vocabulary">
            <h2>1. Match the Words (Pre-reading)</h2>
            <p style="margin-bottom: 1rem; color: #cbd5e1;">Click an English word, then click its Spanish translation.</p>
            <div id="pre-vocab"></div>
        </section>

        <article class="story-text">
            <div class="instruction-notice">
                💡 <strong>Tip:</strong> Double-click or select any word you don't know to translate and save it to <a href="my_vocabulary.html">My Vocabulary</a>!
            </div>
            
            <h2>{story['h2_title']}</h2>
            
            {story['text']}
        </article>

        <section class="quiz">
            <h2>2. Comprehension Quiz (Cuestionario)</h2>
            {quiz_html}
        </section>

        <section class="vocabulary">
            <h2>3. Vocabulary Recall (Post-reading)</h2>
            <p style="margin-bottom: 1rem; color: #cbd5e1;">Test your memory. Type the translation in the box.</p>
            <div id="post-vocab"></div>
        </section>

        <div class="story-navigation">
            <a href="index.html" class="nav-btn secondary">⬅ All Stories</a>
            <a href="my_vocabulary.html" class="nav-btn secondary">📖 My Vocabulary</a>
        </div>
    </main>

    <footer class="main-footer">
        <p>&copy; 2026 Reading English. All rights reserved.</p>
    </footer>

    <script src="js/translator.js"></script>
    <script src="js/story.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const storyVocabulary = {vocab_json};

            window.currentStoryVocabulary = storyVocabulary;
            initMatchingGame('pre-vocab', storyVocabulary);
            initRecallTest('post-vocab', storyVocabulary);
        }});
    </script>
</body>
</html>"""

for story in stories:
    with open(story['filename'], "w", encoding="utf-8") as f:
        f.write(generate_html(story))
    print(f"Created {story['filename']}")
