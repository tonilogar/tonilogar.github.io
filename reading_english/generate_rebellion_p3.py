import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reading English - The Chronos Rebellion: Part 3">
    <title>The Chronos Rebellion: Part 3 - Reading English</title>
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
        <div class="hero story-hero" style="background: linear-gradient(135deg, #1f2937, #065f46);">
            <h1>The Chronos Rebellion: Part 3</h1>
            <p>Level: C1 | The First String & The Quantum Hangover (Past Perfect Continuous)</p>
        </div>
    </header>

    <main class="content story-content">
        <section class="vocabulary">
            <h2>1. Match the Words (Pre-reading)</h2>
            <p style="margin-bottom: 1rem; color: #cbd5e1;">Click an English word, then click its Spanish translation. <strong>Warning: Adult humor and gritty themes.</strong></p>
            <div id="pre-vocab"></div>
        </section>

        <article class="story-text">
            <div class="instruction-notice">
                💡 <strong>Grammar Tip:</strong> This chapter focuses on the <strong>Past Perfect Continuous</strong> (<em>had been running, had been drinking</em>). We use it to talk about an ongoing action in the past that caused a specific result in the past.
            </div>
            
            <h2>Chapter I: The Temporal Hangover</h2>
            
            <p>Traveling through time gave you incredible power, but it also gave you the opportunity to be an absolute disaster. Jack <strong>had been partying</strong> in a 1920s jazz club in Chicago for three days straight. He <strong>had been drinking</strong> illegal whiskey and snorting a futuristic synthetic drug called 'Chronos-Dust' off the bodies of two beautiful jazz singers. When Tenzin finally pulled him back into the quantum portal, Jack was aggressively hungover, half-naked, and extremely angry.</p>
            
            <p>"I was having the time of my life, you bald killjoy!" Jack shouted, putting his pants on while falling over. </p>
            
            <p>"We have a mission," Tenzin replied, his Buddhist patience tested to its absolute limits. "The Grand Algorithm is trying to delete a crucial invention in 60,000 BCE."</p>
            
            <p>Silas Vane, who <strong>had been complaining</strong> all morning about missing a VIP brothel in 17th-century Tortuga, sighed heavily. "Mud, rain, and cavemen. Fantastic. I love my life," Silas muttered sarcastically, lighting a thick cigar.</p>

            <h2>Chapter II: The Bleeding Earth</h2>
            
            <p>They jumped to the Stone Age. The air smelled of wet ash and animal feces. A young human hunter, shivering and covered in mud, was hiding beneath the roots of a giant tree. He <strong>had been running</strong> for hours. The Algorithm's agents—metallic beasts disguised as massive prehistoric wolves—patrolled the forest.</p>
            
            <p>Nyx scanned the area with her cybernetic eyes. "Three cyber-wolves approaching," she said coldly. </p>
            
            <p>"Oh, great. Metallic dogs. Because my headache wasn't bad enough," Jack grumbled. He stepped out of the shadows, cocked his heavy futuristic shotgun, and fired a devastating blast at the first wolf. The beast exploded into pieces of bloody metal and blue sparks. Jack took a long drag from a cigarette. "Boom. Excelsior, you metallic son of a bitch!" he yelled, quoting his favorite comic books.</p>

            <h2>Chapter III: The Weapon of Distance</h2>
            
            <p>The primitive hunter was absolutely terrified. He thought Jack was a loud, smoking god of thunder. Silas walked up to the caveman. "Relax, Tarzan," Silas said, blowing cigar smoke into the caveman's face. </p>
            
            <p>The human <strong>had been carrying</strong> a long piece of dried animal gut to repair his clothes. Silas took it from him, grabbed a flexible branch of yew wood, and aggressively bent it. He tied the string to both ends. He had just forged the first bow in human history.</p>
            
            <p>"Look, buddy," Silas explained, putting a sharpened stick on the string. "You pull this, and you shoot the pointy end into the bad guy. It's like prehistoric Tinder, but instead of swiping right, you penetrate their skulls from a distance. Got it?"</p>

            <h2>Chapter IV: The First Shot</h2>
            
            <p>The hunter obviously didn't understand the sarcastic references, but he understood the weapon. For his entire life, his people <strong>had been fighting</strong> the world with their fragile bodies. Now, he had range.</p>
            
            <p>The two remaining cyber-wolves jumped into the clearing, their jaws glowing with radioactive light. Instead of running, the human stood his ground. He grabbed the bow, his hands shaking, and pulled the string back. He released it. The heavy spear flew through the air and pierced the alpha beast directly in its optical sensor. The machine collapsed.</p>
            
            <p>Jack smiled and blasted the last wolf. "Not bad, caveman. Now go invent the wheel or something so we can get a taxi," Jack joked, rubbing his temples. "I need a painkiller and a hot shower."</p>
            
            <p>Tenzin shook his head, praying to the universe for patience. The power dynamic of the planet had shifted forever, thanks to a monk, a blind girl, and two highly dysfunctional, drug-abusing time travelers.</p>
            
            <p><strong>[End of Part 3. The Rebellion continues...]</strong></p>
        </article>

        <section class="quiz">
            <h2>2. Comprehension Quiz (Cuestionario)</h2>
            <div class="quiz-question">
                <p>1. What had Jack been doing before Tenzin pulled him into the portal?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He had been partying, drinking, and taking Chronos-Dust in a 1920s jazz club.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He had been sleeping peacefully in the Chronos base.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He had been hunting cyber-wolves in the Stone Age.</button>
            </div>
            <div class="quiz-question">
                <p>2. What did Silas say the bow was like?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He said it was like a magic wand for hunting.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He said it was like prehistoric Tinder, but for penetrating skulls.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He said it was a tool to make fire from a distance.</button>
            </div>
            <div class="quiz-question">
                <p>3. Why was the young human hunter hiding under the tree roots?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He had been trying to invent a new weapon.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He was trying to steal Jack's shotgun.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He had been running from the cyber-wolves for hours.</button>
            </div>
            <div class="quiz-question">
                <p>4. What did Jack yell after destroying the first cyber-wolf?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">"Boom. Excelsior, you metallic son of a bitch!"</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">"For the Grand Algorithm and the perfect timeline!"</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">"Peace without freedom is a beautiful cemetery!"</button>
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
            <a href="the_chronos_rebellion_part4.html" class="nav-btn">Next Story ➡</a>
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
                { id: '1', en: 'hungover', es: 'con resaca' },
                { id: '2', en: 'brothel', es: 'burdel' },
                { id: '3', en: 'feces', es: 'heces' },
                { id: '4', en: 'gut', es: 'tripa' },
                { id: '5', en: 'to forge', es: 'forjar' },
                { id: '6', en: 'makeshift', es: 'improvisado' },
                { id: '7', en: 'to pierce', es: 'perforar' },
                { id: '8', en: 'skull', es: 'cráneo' },
                { id: '9', en: 'headache', es: 'dolor de cabeza' },
                { id: '10', en: 'dysfunctional', es: 'disfuncional' }
            ];

            window.currentStoryVocabulary = storyVocabulary;
            initMatchingGame('pre-vocab', storyVocabulary);
            initRecallTest('post-vocab', storyVocabulary);
        });
    </script>
</body>
</html>"""

with open("the_chronos_rebellion_part3.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created the_chronos_rebellion_part3.html")
