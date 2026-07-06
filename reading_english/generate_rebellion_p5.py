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
            <p>Level: C1 | Jack's Wild Escapade (Inversion for Emphasis)</p>
        </div>
    </header>

    <main class="content story-content">
        <section class="vocabulary">
            <h2>1. Match the Words (Pre-reading)</h2>
            <p style="margin-bottom: 1rem; color: #cbd5e1;">Click an English word, then click its Spanish translation. <strong>Warning: Noir themes, heavy drinking, and highly explicit adult situations.</strong></p>
            <div id="pre-vocab"></div>
        </section>

        <article class="story-text">
            <div class="instruction-notice">
                💡 <strong>Grammar Tip:</strong> This chapter uses <strong>Inversion for Emphasis</strong> (e.g., <em>Never had I seen... / Little did they know... / Not only did he...</em>). This advanced structure makes the narration sound dramatic and stylish, perfect for a noir detective.
            </div>
            
            <h2>Chapter I: The Quantum Frustration</h2>
            
            <p>The quantum void was incredibly boring. Tenzin was meditating and Silas was fixing a rusty toaster. I needed a break. I am a detective, a fighter, and a man with very high physical needs. <strong>Never in my life had I felt</strong> so sexually frustrated and trapped inside a floating monastery.</p>
            
            <p>I needed to blow off some serious steam. I wanted strong alcohol, a dark room, and a lot of wild sex. But where can a time traveler go without causing a temporal paradox? </p>
            
            <p>I walked to the portal console and typed in the coordinates for "Orphan Timeline 404". It was a dead-end universe. A pocket dimension containing New York City in 1932, trapped in a perpetual loop just hours before it was deleted by the Algorithm. Nothing I did there would matter. <strong>Rarely do you find</strong> a place so perfectly suited for a consequence-free weekend of pure lust.</p>

            <h2>Chapter II: The Speakeasy Seduction</h2>
            
            <p>I stepped out of the portal into a rainy alley in Manhattan and walked directly into an underground speakeasy. Jazz music filled the room, mixing with the thick cigar smoke.</p>
            
            <p>I sat at the bar and ordered a double whiskey. Next to me sat a gorgeous woman in a tight red silk dress that left very little to the imagination. She had sharp eyes and red lipstick. <strong>Seldom have I seen</strong> a woman who radiated so much raw sexual energy. </p>
            
            <p>"You look like a man who knows exactly what he wants," she whispered, leaning so close I could feel the heat of her body.</p>
            
            <p>"<strong>Little do you know</strong>, sweetheart, I want to ruin that red dress," I replied, lighting her cigarette. We drank heavily, touching hands and legs under the table. The tension was electric. </p>

            <h2>Chapter III: The Unwanted Interruption</h2>
            
            <p>We were standing up to go to a hotel room upstairs when three drunk mobsters walked in. They grabbed a young waitress, laughing aggressively. I sighed. I wanted to go upstairs, but unfortunately, I have a strict moral compass about bullies.</p>
            
            <p><strong>Not only were they</strong> harassing an innocent girl, <strong>but they were also</strong> delaying my sex life. I walked over to them. The biggest mobster pulled out a Tommy gun.</p>
            
            <p>"<strong>Under no circumstances should you</strong> interrupt a man on his way to the bedroom," I warned him coldly.</p>
            
            <p>He laughed and pulled the trigger. <strong>Barely had he moved his finger when I</strong> activated my temporal-shield. The bullets bounced off. I grabbed the Tommy gun, crushed the barrel with my cyber-glove, and violently threw all three men out the window into the rainy street. No casualties, but I definitely broke some bones.</p>

            <h2>Chapter IV: The Climax and The Reset</h2>
            
            <p>The woman in the red dress was breathing heavily, staring at me with wide eyes. "That was... incredibly hot," she whispered. She grabbed my tie and pulled me upstairs to a dark, smoky hotel room.</p>
            
            <p>The next two hours were an absolute blur of intense, passionate, and violent sex. We tore the room apart. <strong>Never had I experienced</strong> a woman so insatiable. We drank whiskey straight from the bottle between rounds, completely lost in each other.</p>
            
            <p>As we lay naked in the tangled sheets, smoking a post-coital cigarette at exactly 3:00 AM, the walls of the hotel room began to dissolve into digital green code. The loop was resetting. The universe was deleting the timeline.</p>
            
            <p>I kissed her one last time as her body started to turn into pixels. <strong>No sooner had we finished</strong> our incredible night <strong>than the entire city</strong> vanished into white noise.</p>
            
            <p>I stepped back into the Chronos base, completely naked, carrying my clothes over my shoulder. I smelled like expensive perfume, sweat, bourbon, and gunpowder. Tenzin looked at me with deep disappointment. I just smiled. Jack was finally relaxed and ready to kill some Algorithm robots.</p>
            
            <p><strong>[End of Part 5. The Rebellion continues...]</strong></p>
        </article>

        <section class="quiz">
            <h2>2. Comprehension Quiz (Cuestionario)</h2>
            <div class="quiz-question">
                <p>1. Why did Jack choose to go to "Orphan Timeline 404"?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because Tenzin told him to investigate a murder there.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">Because it was a deleted loop where he could have consequence-free sex and alcohol.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because he wanted to kill a specific mobster in 1932.</button>
            </div>
            <div class="quiz-question">
                <p>2. What made Jack confront the mobsters in the speakeasy?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">Not only were they harassing an innocent girl, but they were also delaying his date.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He owed them money from a poker game.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">The woman in the red dress asked him to fight them.</button>
            </div>
            <div class="quiz-question">
                <p>3. What happened after Jack threw the mobsters out the window?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">The police raided the bar and arrested Jack.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">The woman found it incredibly hot and pulled him upstairs for intense sex.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">The loop reset immediately and he returned to the base.</button>
            </div>
            <div class="quiz-question">
                <p>4. How did Jack return to the Chronos base?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">Completely naked, carrying his clothes, smelling like perfume, sweat, and bourbon.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Fully dressed and apologizing to Tenzin.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Wounded from the fight with the mobsters.</button>
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
            <a href="the_chronos_rebellion_part6.html" class="nav-btn">Next Story ➡</a>
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
                { id: '1', en: 'lust', es: 'lujuria' },
                { id: '2', en: 'to blow off steam', es: 'desahogarse' },
                { id: '3', en: 'speakeasy', es: 'bar clandestino' },
                { id: '4', en: 'to flirt', es: 'coquetear' },
                { id: '5', en: 'harass', es: 'acosar' },
                { id: '6', en: 'insatiable', es: 'insaciable' },
                { id: '7', en: 'sweat', es: 'sudor' },
                { id: '8', en: 'tangled', es: 'enredado' },
                { id: '9', en: 'disappointment', es: 'decepción' },
                { id: '10', en: 'to dissolve', es: 'disolverse' }
            ];

            window.currentStoryVocabulary = storyVocabulary;
            initMatchingGame('pre-vocab', storyVocabulary);
            initRecallTest('post-vocab', storyVocabulary);
        });
    </script>
</body>
</html>"""

with open("the_chronos_rebellion_part5.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created the_chronos_rebellion_part5.html")
