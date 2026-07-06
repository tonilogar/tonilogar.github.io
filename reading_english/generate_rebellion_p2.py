import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reading English - The Chronos Rebellion: Part 2">
    <title>The Chronos Rebellion: Part 2 - Reading English</title>
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
        <div class="hero story-hero" style="background: linear-gradient(135deg, #0f172a, #b91c1c);">
            <h1>The Chronos Rebellion: Part 2</h1>
            <p>Level: B2+ | The Glass Eye (Modals of Deduction)</p>
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
                💡 <strong>Grammar Tip:</strong> This chapter uses <strong>Modals of Deduction in the Past</strong> (<em>must have, might have, can't have</em>) to make logical guesses about things that already happened.
            </div>
            
            <h2>Chapter I: The Broken Recruits</h2>
            
            <p>The Grand Algorithm wanted humanity to look down at the dirt. If humans looked up at the stars, they would dream of infinity, and infinity was a mathematical variable the Algorithm could not control. Tenzin knew they had to protect a specific moment in history. But to do it, they needed a team.</p>
            
            <p>In a dirty, rain-soaked tavern in an alternate 18th century, Jack found Silas Vane. Silas was an ex-mechanic whose timeline had been deleted. He was staring at a broken pocket watch, drinking heavily. He was terrified of forgetting his dead son's face. Jack looked at the complex mechanical tools on the table. "You <strong>must have been</strong> a master engineer," Jack said. "The Algorithm <strong>can't have erased</strong> your skills. We need you to forge destiny."</p>
            
            <p>Their second recruit was Nyx, a young scout from a dystopian 2099. She survived a mind-wipe by the Algorithm, but the trauma had left her partially blind in the dark. However, her cybernetic implants allowed her to see temporal anomalies. When Tenzin found her shivering in an alley, he touched her shoulder. "You <strong>might have seen</strong> the Algorithm's code when it wiped your city," the Monk deduced softly. "Your fear is a weapon. Come with us."</p>

            <h2>Chapter II: The Dark Workshop (Holland, 1608)</h2>
            
            <p>The four rebels—Tenzin, Jack, Silas, and Nyx—jumped through the quantum void to Middleburg, Holland, in the year 1608. The city was grim, cold, and covered in gray fog. They broke into the dark optical workshop of a man named Hans Lippershey. The smell of cold glass and wet wood filled the room.</p>
            
            <p>Something was wrong. The tools were thrown on the floor. Nyx's mechanical eyes scanned the room. "An agent of the Algorithm <strong>must have been</strong> here," she whispered, trembling. "The timeline is corrupted. The two children who were supposed to discover the telescope <strong>can't have found</strong> the lenses naturally. The agent hid them."</p>
            
            <p>Silas Vane stepped forward, his hands steady despite his inner demons. He picked up two pieces of curved glass—one convex, one concave. "I can fix it," Silas murmured. He carefully calculated the exact distance and angle needed. "The children <strong>might have played</strong> with them right here on the table. I will leave them perfectly aligned." He placed the lenses on the wooden table, pointing directly toward the window.</p>

            <h2>Chapter III: The Distant Weathervane</h2>
            
            <p>The rebels hid in the shadows as the workshop door creaked open. Two young children ran inside, laughing. They started playing with the tools on the table, just as Silas had planned. Suddenly, one of the boys looked through the two aligned lenses that Silas had prepared.</p>
            
            <p>The boy gasped. Through the dirty window, miles away, the bronze weathervane of a distant church suddenly appeared large, clear, and sharp, as if it were right in front of his face. The boy <strong>must have felt</strong> like he was doing magic. He immediately screamed for Master Lippershey.</p>
            
            <p>Lippershey rushed into the room. When he looked through the glass, his eyes widened with shock. He understood the enormous potential of the invention instantly. The telescope was born. But just as Lippershey smiled, the front door exploded. Three cybernetic Watchmen, sent by the Algorithm, entered the shop. "They <strong>must have tracked</strong> our temporal jump!" Jack shouted, pulling out his heavy shotgun. "Silas, Nyx, get to the portal! We are jumping to Italy!"</p>

            <h2>Chapter IV: The Stargazer (Padua, 1609)</h2>
            
            <p>They escaped the burning workshop and landed in a dark garden in Padua, Italy, a year later. The night sky was terrifyingly clear, the stars staring down like cold, calculating eyes. Standing on the balcony was a man holding a refined, longer version of the Dutch invention. It was Galileo Galilei.</p>
            
            <p>Galileo hesitated. A dark, unnatural shadow—a manifestation of the Algorithm—was whispering in his ear, telling him to look down at the safe, predictable earth. If he looked up, his life would be filled with persecution and pain.</p>
            
            <p>Nyx stepped out of the darkness. Her own fear of blindness made her understand his hesitation. She walked up to Galileo and whispered, "The darkness is terrifying, but it is not empty. Look."</p>
            
            <p>Galileo took a deep breath, raised the telescope, and pointed it at the moon, and then at the infinite stars of the Milky Way. The universe expanded in his mind. The mathematical prison of the Algorithm cracked. Tenzin smiled peacefully in the garden below. "He <strong>must have realized</strong>," the Monk thought, "how mathematically small we are... and how infinitely big our freedom is."</p>
            
            <p><strong>[End of Part 2. The Rebellion continues...]</strong></p>
        </article>

        <section class="quiz">
            <h2>2. Comprehension Quiz (Cuestionario)</h2>
            <div class="quiz-question">
                <p>1. What did Jack deduce about Silas Vane when he saw the tools?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He must have been a soldier.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He must have been a master engineer.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He can't have known how to fight.</button>
            </div>
            <div class="quiz-question">
                <p>2. Why did Nyx think an agent of the Algorithm had been in the workshop?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because Hans Lippershey was dead.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because Galileo was hiding there.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">Because the tools were thrown on the floor and the timeline was corrupted.</button>
            </div>
            <div class="quiz-question">
                <p>3. What did the young boy see through the aligned lenses?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">A distant church weathervane looking large and clear.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">The Grand Algorithm in the sky.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">A Watchmaker assassin.</button>
            </div>
            <div class="quiz-question">
                <p>4. What did Galileo Galilei do at the end of the story?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He raised the telescope and pointed it at the moon and the stars.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He destroyed the telescope because he was afraid.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He fought the cybernetic Watchmen.</button>
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
            <a href="the_chronos_rebellion_part3.html" class="nav-btn">Next Story ➡</a>
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
                { id: '1', en: 'lens', es: 'lente' },
                { id: '2', en: 'to forge', es: 'forjar' },
                { id: '3', en: 'anomaly', es: 'anomalía' },
                { id: '4', en: 'workshop', es: 'taller' },
                { id: '5', en: 'weathervane', es: 'veleta' },
                { id: '6', en: 'to hesitate', es: 'dudar' },
                { id: '7', en: 'deduction', es: 'deducción' },
                { id: '8', en: 'implant', es: 'implante' },
                { id: '9', en: 'persecution', es: 'persecución' },
                { id: '10', en: 'to wipe', es: 'borrar' }
            ];

            window.currentStoryVocabulary = storyVocabulary;
            initMatchingGame('pre-vocab', storyVocabulary);
            initRecallTest('post-vocab', storyVocabulary);
        });
    </script>
</body>
</html>"""

with open("the_chronos_rebellion_part2.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created the_chronos_rebellion_part2.html")
