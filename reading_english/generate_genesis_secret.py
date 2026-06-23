import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reading English - The Chronos Genesis: Part 2">
    <title>The Chronos Genesis: Part 2 - Reading English</title>
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
        <div class="hero story-hero" style="background: linear-gradient(135deg, #1e3a8a, #4c1d95);">
            <h1>The Chronos Genesis: Part 2</h1>
            <p>Level: B1 | The Secret Son</p>
        </div>
    </header>

    <main class="content story-content">
        <section class="vocabulary">
            <h2>1. Match the Words (Pre-reading)</h2>
            <p style="margin-bottom: 1rem; color: #cbd5e1;">Click an English word, then click its Spanish translation. This story uses B1 vocabulary.</p>
            <div id="pre-vocab"></div>
        </section>

        <article class="story-text">
            <div class="instruction-notice">
                💡 <strong>Tip:</strong> This is a Mega-Story. It is divided into chapters. Take your time. Double-click any word you don't know to save it to your vocabulary!
            </div>
            
            <h2>Chapter I: The Broken Vow</h2>
            
            <p>After creating the Chronos Agency, Tenzin spent hundreds of years alone in the quantum void. The emptiness of the universe was beautiful, but the loneliness was terrible. Although he was a monk who had promised to avoid worldly desires, he was still human. One day, he couldn't stand the isolation anymore. He decided to visit ancient India in the 3rd century BCE, just to feel the sun on his face and hear people talking.</p>
            
            <p>There, he met a woman named Dharma. She had a pure soul and a beautiful smile. For the first time in his long life, Tenzin let himself feel romantic love. He broke his monk vows. They spent a wonderful year together, and Dharma had a son. Tenzin loved the baby unconditionally. However, his happiness was destroyed when he realized that The Order was searching the timeline for him.</p>
            
            <p>"I wish I hadn't left the void," Tenzin thought with deep sadness. "If I stay here, The Order will find my family and kill them to hurt me." To protect Dharma and his son, Tenzin had to return to the agency. He abandoned them without saying goodbye. "I regret leaving them," he whispered, watching them from the stars, "but it is the only way to keep them safe."</p>

            <h2>Chapter II: The Bloody Emperor</h2>
            
            <p>From his floating temple in the void, Tenzin watched his son grow up. Without a father, the boy grew angry and ambitious. His name was Ashoka. He joined the army and quickly became a powerful, cruel general. Eventually, he became the Emperor of India.</p>
            
            <p>Ashoka used to be a sweet child, but now he was a monster. He started a massive war to conquer the neighboring lands. Tenzin watched the battles with tears in his eyes. Thousands of people were dying because of his son. The timeline was shaking. Ashoka was not a Nexus Point, but his actions were causing immense suffering.</p>
            
            <p>"If only I had been there to teach him," Tenzin cried. "He is destroying the world because he doesn't know how to love. This is my fault. My carnal desire created a tyrant." Tenzin knew he shouldn't interfere with personal matters, but the guilt was too heavy. He had to fix his mistake.</p>

            <h2>Chapter III: The Wandering Monk</h2>
            
            <p>The war of Kalinga was over. Emperor Ashoka was standing in the middle of a battlefield. The ground was red, and there were thousands of dead bodies everywhere. For the first time, Ashoka felt a terrible emptiness in his heart. Victory didn't feel good; it felt like poison.</p>
            
            <p>Suddenly, an old man in orange robes walked through the battlefield. It was Tenzin, in disguise as a wandering monk. He approached the powerful Emperor without fear. Ashoka's guards raised their swords, but the Emperor stopped them. "Who are you?" Ashoka asked, looking at the peaceful man.</p>
            
            <p>"I am just a teacher," Tenzin said softly, looking into his son's eyes. He felt an overwhelming wave of unconditional love, but he hid his emotions perfectly. "I see a king who has conquered the world, but who cannot conquer his own mind. I have come to train you."</p>

            <h2>Chapter IV: The Final Lesson</h2>
            
            <p>For several months, Tenzin stayed in the palace. He didn't teach Ashoka how to fight; he taught him how to breathe, how to meditate, and how to feel compassion. He trained his son's spirit. Tenzin used to teach young monks in the Himalayas, but this was the most important lesson of his entire existence.</p>
            
            <p>Slowly, the cruel Emperor changed. Ashoka stopped all wars. He built hospitals, protected animals, and spread the message of Buddhism across the world. He became one of the greatest and most peaceful rulers in history. He changed the world forever, but he never knew that his mysterious teacher was his father.</p>
            
            <p>When the training was complete, Tenzin knew he had to leave. He stood by Ashoka's bed while the Emperor was sleeping. He touched his son's forehead gently. "I am sorry I cannot be a father to you," Tenzin whispered, crying silently. "But I will always be your guardian."</p>
            
            <p>Tenzin returned to the quantum void. His heart was broken, but it was also full of peace. His greatest weakness—his human desire—had ultimately brought the greatest light to the universe.</p>
            
            <p><strong>[End of Part 2]</strong></p>
        </article>

        <section class="quiz">
            <h2>2. Comprehension Quiz (Cuestionario)</h2>
            <div class="quiz-question">
                <p>1. Why did Tenzin leave his family in ancient India?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because he didn't love them</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">Because he wanted to protect them from The Order</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because he wanted to conquer the world</button>
            </div>
            <div class="quiz-question">
                <p>2. What happened to Ashoka when he grew up?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He became a peaceful monk immediately</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He traveled to the quantum void</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He became a powerful and cruel Emperor</button>
            </div>
            <div class="quiz-question">
                <p>3. What did Tenzin teach his son?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He taught him meditation and compassion</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He taught him how to use a sword</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He taught him how to build a time machine</button>
            </div>
            <div class="quiz-question">
                <p>4. Did Ashoka know that Tenzin was his father?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Yes, Tenzin told him at the end</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">No, he never knew the truth</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Yes, his mother told him</button>
            </div>
        </section>

        <section class="vocabulary">
            <h2>3. Vocabulary Recall (Post-reading)</h2>
            <p style="margin-bottom: 1rem; color: #cbd5e1;">Test your memory. Type the translation in the box.</p>
            <div id="post-vocab"></div>
        </section>

        <div class="story-navigation">
            <a href="index.html" class="nav-btn secondary">⬅ All Stories</a>
            <a href="my_vocabulary.html" class="nav-btn secondary">📖 My Vocabulary</a>
            <a href="the_chronos_genesis_part3.html" class="nav-btn">Next Story ➡</a>
        </div>
    </main>

    <footer class="main-footer">
        <p>&copy; 2026 Reading English. All rights reserved.</p>
    </footer>

    <script src="js/translator.js"></script>
    <script src="js/story.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const storyVocabulary = [
                { id: '1', en: 'vow', es: 'voto (promesa)' },
                { id: '2', en: 'loneliness', es: 'soledad' },
                { id: '3', en: 'guilt', es: 'culpa' },
                { id: '4', en: 'cruel', es: 'cruel' },
                { id: '5', en: 'disguise', es: 'disfraz' },
                { id: '6', en: 'to regret', es: 'arrepentirse' },
                { id: '7', en: 'unconditional', es: 'incondicional' },
                { id: '8', en: 'ruler', es: 'gobernante' }
            ];

            initMatchingGame('pre-vocab', storyVocabulary);
            initRecallTest('post-vocab', storyVocabulary);
        });
    </script>
</body>
</html>"""

with open("the_chronos_genesis_secret.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created the_chronos_genesis_secret.html")
