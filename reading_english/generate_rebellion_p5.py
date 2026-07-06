import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reading English - The Chronos Rebellion: Part 5">
    <title>The Chronos Rebellion: Part 5 - Reading English</title>
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
        <div class="hero story-hero" style="background: linear-gradient(135deg, #18181b, #7e22ce);">
            <h1>The Chronos Rebellion: Part 5</h1>
            <p>Level: C1 | Jack's Escapade (Inversion for Emphasis)</p>
        </div>
    </header>

    <main class="content story-content">
        <section class="vocabulary">
            <h2>1. Match the Words (Pre-reading)</h2>
            <p style="margin-bottom: 1rem; color: #cbd5e1;">Click an English word, then click its Spanish translation. <strong>Warning: Noir themes, alcohol, and adult humor.</strong></p>
            <div id="pre-vocab"></div>
        </section>

        <article class="story-text">
            <div class="instruction-notice">
                💡 <strong>Grammar Tip:</strong> This chapter uses <strong>Inversion for Emphasis</strong> (e.g., <em>Never had I seen... / Little did they know... / Not only did he...</em>). This advanced structure makes the narration sound dramatic and stylish, perfect for a noir detective.
            </div>
            
            <h2>Chapter I: The Quantum Boredom</h2>
            
            <p>The quantum void was incredibly boring. Tenzin was meditating, Silas was fixing a rusty toaster, and Nyx was sleeping. I needed a break. I am a detective, a fighter, a man who appreciates good tobacco, strong alcohol, and dangerous women. <strong>Never in my life had I felt</strong> so trapped inside a floating monastery.</p>
            
            <p>I needed to blow off some steam. I wanted to be completely alone, without rules, without the Grand Algorithm watching me. But where can a time traveler go without causing a temporal paradox? </p>
            
            <p>I walked to the portal console and typed in the coordinates for "Orphan Timeline 404". It was a dead-end universe. A pocket dimension containing New York City in 1932, trapped in a perpetual loop just hours before it was deleted by the Algorithm. Nothing I did there would matter. <strong>Rarely do you find</strong> a place so perfectly suited for a consequence-free weekend.</p>

            <h2>Chapter II: The End of the World Speakeasy</h2>
            
            <p>I stepped out of the portal into a dark, rainy alley in Manhattan. The air smelled of wet asphalt and cheap gin. I walked into an underground speakeasy called <em>The Blue Paradox</em>. Jazz music filled the room, mixing with the thick cigar smoke.</p>
            
            <p>I sat at the bar and ordered a double whiskey. Next to me sat a woman in a red silk dress. She had sharp eyes and a cynical smile. <strong>Seldom have I seen</strong> a woman drink bourbon with such elegant ferocity. </p>
            
            <p>"You look like a man who's running from the clock," she said, offering me a cigarette.</p>
            
            <p>"<strong>Little do you know</strong>, sweetheart, I am the clock," I replied, lighting both our cigarettes with a futuristic plasma lighter. We drank, laughed, and flirted. For a few hours, the war against the Algorithm completely disappeared from my mind.</p>

            <h2>Chapter III: The Moral Code</h2>
            
            <p>I wanted to be bad tonight, but unfortunately, I have a stupid moral compass. I try not to hurt anyone unless absolutely necessary. Suddenly, three drunk mobsters walked in and started violently harassing a young waitress, dropping her tray of glasses.</p>
            
            <p>I sighed. <strong>Not only were they</strong> ruining the jazz music, <strong>but they were also</strong> ruining my date. I walked over to them. The biggest mobster pulled out a Tommy gun.</p>
            
            <p>"<strong>Under no circumstances should you</strong> point that at me," I warned him calmly, taking a drag from my cigarette.</p>
            
            <p>He laughed and pulled the trigger. <strong>Barely had he moved his finger when I</strong> activated my temporal-shield. The bullets bounced off an invisible wall. I grabbed the Tommy gun, crushed the barrel with my cyber-glove, and threw all three men out the window into the rainy street without breaking a sweat. No casualties, just severely bruised egos.</p>

            <h2>Chapter IV: The Reset</h2>
            
            <p>The entire bar was staring at me in absolute silence. Then, the jazz band started playing again, even louder. The woman in the red dress smiled and raised her glass to me.</p>
            
            <p>We spent the rest of the night drinking, talking about our regrets, and enjoying the beautiful illusion of the 1930s. I was completely relaxed. At exactly 3:00 AM, the walls of the speakeasy began to dissolve into digital green code. The loop was resetting. The universe was deleting the timeline to start over.</p>
            
            <p>I finished my whiskey, put a solid gold Roman coin on the bar as a tip, and kissed the woman's hand. <strong>No sooner had I stepped</strong> back into the portal <strong>than the entire city</strong> vanished into white noise.</p>
            
            <p>I arrived back at the Chronos base, smelling like cheap perfume, bourbon, and gunpowder. I was smiling. I was finally ready to go back to work and destroy that math-obsessed Algorithm.</p>
            
            <p><strong>[End of Part 5. The Rebellion continues...]</strong></p>
        </article>

        <section class="quiz">
            <h2>2. Comprehension Quiz (Cuestionario)</h2>
            <div class="quiz-question">
                <p>1. Why did Jack choose to go to "Orphan Timeline 404"?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because Tenzin told him to investigate a murder there.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">Because it was a deleted loop where nothing he did would affect the main universe.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because he wanted to kill a specific mobster in 1932.</button>
            </div>
            <div class="quiz-question">
                <p>2. How did Jack respond when the mobster pulled the trigger?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He activated his temporal-shield and the bullets bounced off.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He shot the mobster first with his futuristic shotgun.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He dodged the bullets and ran out the back door.</button>
            </div>
            <div class="quiz-question">
                <p>3. What happened at exactly 3:00 AM in the speakeasy?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">The police raided the bar and arrested Jack.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Jack proposed to the woman in the red dress.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">The loop reset and the city began to dissolve into digital code.</button>
            </div>
            <div class="quiz-question">
                <p>4. What did Jack leave as a tip on the bar?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">A solid gold Roman coin.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">A futuristic plasma lighter.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">A hundred dollar bill from 1932.</button>
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
            <a href="index.html" class="nav-btn">Back to Index ➡</a>
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
                { id: '1', en: 'boredom', es: 'aburrimiento' },
                { id: '2', en: 'to blow off steam', es: 'desahogarse' },
                { id: '3', en: 'speakeasy', es: 'bar clandestino' },
                { id: '4', en: 'to flirt', es: 'coquetear' },
                { id: '5', en: 'harass', es: 'acosar' },
                { id: '6', en: 'trigger', es: 'gatillo' },
                { id: '7', en: 'to bounce', es: 'rebotar' },
                { id: '8', en: 'barrel', es: 'cañón' },
                { id: '9', en: 'bruised', es: 'magullado' },
                { id: '10', en: 'to dissolve', es: 'disolverse' }
            ];

            initMatchingGame('pre-vocab', storyVocabulary);
            initRecallTest('post-vocab', storyVocabulary);
        });
    </script>
</body>
</html>"""

with open("the_chronos_rebellion_part5.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created the_chronos_rebellion_part5.html")
