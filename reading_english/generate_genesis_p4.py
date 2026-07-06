import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reading English - The Chronos Genesis: Part 4">
    <title>The Chronos Genesis: Part 4 - Reading English</title>
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
            <h1>The Chronos Genesis: Part 4</h1>
            <p>Level: B1+ | The Architect of The Order</p>
        </div>
    </header>

    <main class="content story-content">
        <section class="vocabulary">
            <h2>1. Match the Words (Pre-reading)</h2>
            <p style="margin-bottom: 1rem; color: #cbd5e1;">Click an English word, then click its Spanish translation. This story uses B1+ vocabulary.</p>
            <div id="pre-vocab"></div>
        </section>

        <article class="story-text">
            <div class="instruction-notice">
                💡 <strong>Tip:</strong> This is a Mega-Story. It explores deep philosophical themes. Double-click any word you don't know to save it to your vocabulary!
            </div>
            
            <h2>Chapter I: The God Particle</h2>
            
            <p>It was the year 2450. The Earth was a highly advanced but deeply traumatized planet. Humanity had survived terrible wars and climate disasters, and the survivors lived in massive, peaceful cities. In the most advanced laboratory in the world, two brilliant scientists stood in front of a glowing, transparent crystal. They were Dr. Aris and Dr. Victor Kaelen.</p>
            
            <p>They had just isolated the Chronos Particle. For the first time in human history, they held the power to travel through time.</p>
            
            <p>"We have done it, Victor," Dr. Aris said, staring at the crystal. He felt a deep sense of fear. "Even though we have discovered this power, we must never use it. If we alter the timeline, the consequences will be catastrophic. We should only observe the past, never touch it."</p>
            
            <p>Dr. Kaelen did not smile. He looked at the crystal with absolute obsession. "If humanity were perfect, I would agree with you, Aris," Kaelen replied coldly. "But look at our history. Millions have died in useless wars. Children have suffered terrible diseases. If we had possessed this technology centuries ago, those people wouldn't have suffered. We have a moral obligation to cure reality."</p>

            <h2>Chapter II: The Perfect Cage</h2>
            
            <p>Dr. Aris stepped back. He was shocked by his friend's words. "You can't be serious! If we rewrite history to eliminate pain, we will also eliminate free will. Human beings learn from their mistakes. You are talking about playing God."</p>
            
            <p>Kaelen's eyes became dark with anger. "Don't talk to me about God, Aris! Did God save my daughter during the London Ashes?" He was talking about a terrible event ten years ago, when a rebel bomb had destroyed half of the city. Kaelen had lost his family. "I am doing this for her. I will erase that war. I will be the Architect of a perfect timeline."</p>
            
            <p>Aris looked at him with deep sadness. He realized that Kaelen wasn't trying to save the world; he was just using his personal tragedy as an excuse. His massive ego was hiding behind his grief. "A perfect cage is still a cage, Victor!" Aris shouted. "If you take away our ability to choose, we are no longer human. We are just machines following your script."</p>
            
            <p>Kaelen shook his head slowly. "I prefer a cage of peace to an ocean of blood. Provided that nobody suffers, I don't care about free will."</p>

            <h2>Chapter III: The Betrayal</h2>
            
            <p>The next day, Aris reported Kaelen's dangerous ideas to the Scientific Council. However, he was completely unprepared for what happened next. When Aris arrived at the Council Chamber, he saw that the guards were wearing new, black armor. The Council members were standing behind Dr. Kaelen, looking at Aris with cold, empty eyes.</p>
            
            <p>"I warned them that your mind was too weak to embrace the future," Kaelen said. "The Council agrees with me. From today, this laboratory is no longer a scientific institution. We are 'The Order'. Our mission is to clean the timeline, century by century, until the universe is perfect."</p>
            
            <p>Aris realized the horrible truth: Kaelen had been secretly manipulating the Council for months. He had built an army while Aris was working in the lab. The black-armored soldiers raised their futuristic weapons and pointed them at Aris.</p>
            
            <p>"Arrest him," Kaelen ordered. "But do not kill him. He is still my friend, even though he is a fool."</p>

            <h2>Chapter IV: The Paradox of Ego</h2>
            
            <p>Aris had to act fast. Using a remote device hidden in his pocket, he caused a massive power failure. In the darkness, he ran to the central laboratory, shot a guard, and stole the glowing Chronos Core. He activated an emergency temporal pod and launched himself randomly into the past, bleeding heavily.</p>
            
            <p>Kaelen broke into the empty room just as the pod disappeared. He screamed in frustration. Suddenly, the residual quantum energy from the Core began to glow in the center of the room. The energy formed the astral projection of an old man wearing orange robes. It was Tenzin, speaking directly from the quantum void across time.</p>
            
            <p>Kaelen stared at the monk. "Who are you?"</p>
            
            <p>"I am the Keeper of the timeline you are trying to break," Tenzin's voice echoed peacefully. "I feel your pain, Victor. But your noble excuse is a lie. This is the paradox of The Order: you want to create a universe completely controlled by you, but you cannot even control yourself. You cannot control your own grief."</p>
            
            <p>"I am going to save humanity!" Kaelen screamed, pulling out a weapon.</p>
            
            <p>"You are not God, Victor," Tenzin said, shaking his head. "Your ego is above you. It is blinding you. As long as you try to control the river of time, I will be there to fight you." The astral projection faded into nothing, leaving Dr. Kaelen alone in the dark. The multiversal war had officially begun.</p>
            
            <p><strong>[End of Part 4]</strong></p>
        </article>

        <section class="quiz">
            <h2>2. Comprehension Quiz (Cuestionario)</h2>
            <div class="quiz-question">
                <p>1. What did Dr. Aris believe they should do with the Chronos Particle?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">They should use it to win wars</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">They should never use it to touch the past</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">They should give it to The Order</button>
            </div>
            <div class="quiz-question">
                <p>2. Why did Dr. Kaelen want to rewrite history?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">To eliminate pain, suffering, and war</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because he wanted to be rich</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because he hated Dr. Aris</button>
            </div>
            <div class="quiz-question">
                <p>3. According to Tenzin, what is Kaelen's real problem?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He doesn't have enough power</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He needs more soldiers</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">His ego is above him and he cannot control his own grief</button>
            </div>
            <div class="quiz-question">
                <p>4. How did Tenzin speak to Dr. Kaelen in the 25th century?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">Through an astral projection from the quantum void</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He called him on a mobile phone</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He traveled there in a spaceship</button>
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
            <a href="the_chronos_protocol_part4.html" class="nav-btn">Next Story ➡</a>
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
                { id: '1', en: 'architect', es: 'arquitecto' },
                { id: '2', en: 'to cure', es: 'curar' },
                { id: '3', en: 'betrayal', es: 'traición' },
                { id: '4', en: 'cage', es: 'jaula' },
                { id: '5', en: 'free will', es: 'libre albedrío' },
                { id: '6', en: 'humanity', es: 'humanidad' },
                { id: '7', en: 'particle', es: 'partícula' },
                { id: '8', en: 'to steal', es: 'robar' }
            ];

            initMatchingGame('pre-vocab', storyVocabulary);
            initRecallTest('post-vocab', storyVocabulary);
        });
    </script>
</body>
</html>"""

with open("the_chronos_genesis_part4.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created the_chronos_genesis_part4.html")
