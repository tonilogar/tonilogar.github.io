import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reading English - The Chronos Rebellion: Part 4">
    <title>The Chronos Rebellion: Part 4 - Reading English</title>
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
        <div class="hero story-hero" style="background: linear-gradient(135deg, #450a0a, #d97706);">
            <h1>The Chronos Rebellion: Part 4</h1>
            <p>Level: C1 | The Leper, The King & The Orgy (Wishes & Regrets)</p>
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
                💡 <strong>Grammar Tip:</strong> This chapter uses <strong>Wishes and Regrets</strong> (<em>I wish I had, If only I could</em>) to express deep sorrow about the past or present. Notice the structure: Wish + Past (for present wishes) or Wish + Past Perfect (for past regrets).
            </div>
            
            <h2>Chapter I: The Terrible Lesson</h2>
            
            <p>The Grand Algorithm was fracturing humanity into isolated tribes. To counter this, Tenzin decided they needed an empire. A violent, bloody empire to forcefully spread philosophy and science. Dr. Kaelen volunteered for the traumatic task of shaping the boy who would become Alexander the Great.</p>
            
            <p>In Pella, Macedonia (351 BCE), five-year-old Alexander was playing in the gardens. Suddenly, Kaelen stepped out of the bushes, heavily disguised as a horrifying leper with rotting skin. Kaelen coughed dramatically, scaring the kid. Then, he broke character, sighed, and pulled a futuristic flask of vodka from his dirty robes.</p>
            
            <p>"Look, kid. <strong>I wish I was</strong> at a beach resort in Malibu right now, drinking a piña colada," Kaelen grumbled, taking a long sip of vodka. "But we have a timeline to save. The world is a monster. To build a library, you must first burn a city. You will love science, but you must become a butcher. Got it? Good. Now, if you'll excuse me, this fake leprosy is incredibly itchy."</p>

            <h2>Chapter II: The Philosopher Butcher</h2>
            
            <p>Years later, Alexander the Great marched his massive armies across the known world. He was a bizarre paradox. In his tent at night, he studied Aristotle's physics and wept over ancient poetry. But his private life was also an absolute hedonistic mess of wine, sex, and extreme violence.</p>
            
            <p>During an incredibly wild orgy in Babylon—filled with naked bodies, Persian wine, and his beautiful lover Hephaestion—Alexander suddenly felt a deep, existential depression. He was completely covered in wine and blood from the morning's battle. The internal contradiction was destroying him.</p>
            
            <p>"<strong>If only I hadn't listened</strong> to that drunk leper," Alexander thought to himself, staring blankly at a naked concubine who was feeding him grapes. "<strong>I wish I could just read</strong> the stars in peace. <strong>I wish I didn't have to</strong> conquer through fear."</p>
            
            <p>Suddenly, the massive wooden doors of the palace exploded. Cybernetic assassins, sent by the Algorithm, interrupted the orgy. Alexander groaned. He picked up his sword, completely naked, and began decapitating metallic robots while making terrible jokes about their lack of anatomy.</p>

            <h2>Chapter III: The Heavy Crown</h2>
            
            <p>In the Chronos void, Tenzin watched the young king fighting naked through the quantum monitors. Nyx and Jack were watching too, eating popcorn.</p>
            
            <p>"We broke him," Nyx whispered. "We turned a philosopher into a mass-murdering sex addict to save the timeline."</p>
            
            <p>"Hey, don't judge. The kid's got good cardio," Jack laughed, chewing on a popcorn kernel. "Excelsior, Lex! Slice that toaster!"</p>
            
            <p>Tenzin closed his eyes, his Buddhist soul heavy with karma. "<strong>If only there were</strong> another way," Tenzin replied softly, ignoring Jack's inappropriate commentary. "Alexander is carrying the sins of the universe on his shoulders. <strong>I wish I could take</strong> his pain away."</p>

            <h2>Chapter IV: The Final Rest</h2>
            
            <p>Babylon, 323 BCE. Alexander lay in his bed, dying of a mysterious fever (and probably too much ancient STDs) at the young age of thirty-two. The palace was silent. His generals wept outside the golden doors.</p>
            
            <p>Tenzin materialized by his bedside. The king opened his tired eyes and looked at the Monk. Despite the fever, Alexander smiled.</p>
            
            <p>"I know you," Alexander whispered. "You're friends with the drunk leper."</p>
            
            <p>"I am," Tenzin said, kneeling beside the bed. "You unified the world, Alexander. You created the Hellenistic era. Science and art will flourish because of your blood. You won the war."</p>
            
            <p>Alexander coughed. The terrible, violent noise in his head—the roar of battles, the screaming, the wild orgies—finally stopped. He felt an absolute, profound silence. He had waited for this rest his entire life.</p>
            
            <p>"At last..." Alexander sighed, exhaling his final breath. "The stars... are so quiet. And tell the leper... he owes me a drink."</p>
            
            <p>The king's conscience finally found peace. Tenzin bowed his head in deep respect, fading back into the quantum void. The Algorithm's grip on Earth had been shattered by the most glorious, disastrous human in history.</p>
            
            <p><strong>[End of Part 4. The Rebellion continues...]</strong></p>
        </article>

        <section class="quiz">
            <h2>2. Comprehension Quiz (Cuestionario)</h2>
            <div class="quiz-question">
                <p>1. What did Kaelen do while disguised as a leper?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He broke character, complained about wanting a piña colada, and drank vodka.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He tried to kill the young Alexander.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He gave Alexander a magical sword.</button>
            </div>
            <div class="quiz-question">
                <p>2. What was Alexander doing when he felt a deep, existential depression?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He was praying in a temple.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He was in the middle of a wild orgy in Babylon, covered in wine and blood.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He was reading a book by Aristotle.</button>
            </div>
            <div class="quiz-question">
                <p>3. How did Jack react to watching Alexander fight the assassins naked?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He felt terrible and wished he could help him.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He ate popcorn, laughed, and praised Alexander's cardio.</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He was disgusted and turned off the monitor.</button>
            </div>
            <div class="quiz-question">
                <p>4. What were Alexander's final words?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">"I wish I had conquered more lands."</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">"The Algorithm will destroy you."</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">"The stars... are so quiet. And tell the leper... he owes me a drink."</button>
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
            <a href="the_chronos_rebellion_part5.html" class="nav-btn">Next Story ➡</a>
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
                { id: '1', en: 'leper', es: 'leproso' },
                { id: '2', en: 'butcher', es: 'carnicero' },
                { id: '3', en: 'orgy', es: 'orgía' },
                { id: '4', en: 'hedonistic', es: 'hedonista' },
                { id: '5', en: 'naked', es: 'desnudo' },
                { id: '6', en: 'to decapitate', es: 'decapitar' },
                { id: '7', en: 'fever', es: 'fiebre' },
                { id: '8', en: 'killjoy', es: 'aguafiestas' },
                { id: '9', en: 'addict', es: 'adicto' },
                { id: '10', en: 'to flourish', es: 'florecer' }
            ];

            window.currentStoryVocabulary = storyVocabulary;
            initMatchingGame('pre-vocab', storyVocabulary);
            initRecallTest('post-vocab', storyVocabulary);
        });
    </script>
</body>
</html>"""

with open("the_chronos_rebellion_part4.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created the_chronos_rebellion_part4.html")
