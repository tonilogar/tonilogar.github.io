import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reading English - The Chronos Protocol: Part 3">
    <title>The Chronos Protocol: Part 3 - Reading English</title>
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
        <div class="hero story-hero">
            <h1>The Chronos Protocol: Part 3</h1>
            <p>Level: A2+ | Focus: Future Tense & Conditionals</p>
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
            
            <h2>The Siege of Chronos</h2>
            
            <p>Jack opened his eyes quickly. He was not in his dark city. He was not in his old bar. He was back in the Chronos Agency. The beautiful stars were still shining outside the window, but the agency was completely different. The lights were flashing red <strong>dangerously</strong>. A loud alarm was ringing.</p>
            
            <p>He remembered everything. He didn't forget the Titanic. He remembered Mr. Sterling and the little girl.</p>
            
            <p>"Why do I remember?" Jack asked loudly.</p>
            
            <p>"Because the timeline is broken," a woman's voice answered. Jack turned around. A tall woman in a futuristic silver uniform was standing near him. She was holding a large weapon <strong>tightly</strong>. "I am Captain Elara. I come from the year 2150. If we don't hurry, we <strong>will die</strong> here."</p>
            
            <p>Jack looked at her. "Where is The Monk?"</p>
            
            <p>"He is in the Hall of Fallen Legends," Elara said <strong>sadly</strong>. "The Order tracked your quantum signal from 1912. They are attacking the agency right now. They <strong>will destroy</strong> everything if we don't protect him."</p>
            
            <p>Jack picked up a weapon from the floor. He felt adrenaline in his blood. "I <strong>will help</strong> you. If they break the main door, we <strong>will fight</strong> them together."</p>
            
            <p>They ran <strong>fast</strong> to the Hall of Fallen Legends. The Monk was sitting on the floor in the center of the statues. He was bleeding, but his face was perfectly calm. He was meditating <strong>quietly</strong>.</p>
            
            <p>"Monk! We <strong>will take</strong> you to a safe time!" Jack shouted. "We <strong>won't let</strong> them kill you."</p>
            
            <p>The Monk opened his eyes slowly. "You remembered the mission, Jack. That means you are not a normal recruit anymore. You are a true Keeper now. I <strong>will not leave</strong> this place. If I leave, the universe <strong>will fall</strong> into chaos."</p>
            
            <p>Suddenly, the massive metal doors exploded <strong>loudly</strong>. Ten soldiers from The Order walked in. They were wearing black armor. Their leader pointed a glowing gun at The Monk.</p>
            
            <p>"The time of anarchists is over," the leader said <strong>coldly</strong>. "We <strong>will rule</strong> the past and the future."</p>
            
            <p>Captain Elara looked at Jack. "If we shoot now, we <strong>will have</strong> a chance," she whispered.</p>
            
            <p>Before they could shoot, The Monk stood up. He raised his hands <strong>calmly</strong>. The air in the room stopped moving. The soldiers from The Order froze completely. The bullets stopped in the air. Time stopped.</p>
            
            <p>The Monk looked at Jack and Elara. "I am holding the time here, but I <strong>will not hold</strong> it forever. My energy is ending."</p>
            
            <p>"What <strong>will happen</strong> to you?" Jack asked. He was very worried.</p>
            
            <p>"I <strong>will become</strong> a statue in this hall," The Monk smiled peacefully. "But the agency <strong>will survive</strong>. Elara, you <strong>will be</strong> the new captain. Jack... <strong>will you return</strong> to your sad life, or <strong>will you stay</strong> here and protect the universe?"</p>
            
            <p>Jack looked at the frozen soldiers. He looked at Elara, and he looked at the beautiful stars outside. His old life was boring and grey. This was where he belonged.</p>
            
            <p>"I <strong>won't go</strong> back," Jack said <strong>firmly</strong>. "I <strong>will stay</strong>."</p>
            
            <p>The Monk nodded. His body slowly turned into white stone. He became the most beautiful statue in the Hall of Fallen Legends. Time started moving again, but the soldiers from The Order disappeared into dust. The agency was safe.</p>
            
            <p>Captain Elara touched Jack's shoulder. "Welcome to the team, Keeper Jack. Tomorrow, we <strong>will have</strong> a lot of work."</p>
        </article>

        <section class="quiz">
            <h2>2. Comprehension Quiz (Cuestionario)</h2>
            <div class="quiz-question">
                <p>1. Why did Jack remember his mission on the Titanic?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">Because the timeline was broken</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because The Monk gave him medicine</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because he is an alien</button>
            </div>
            <div class="quiz-question">
                <p>2. Who is Captain Elara?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">She is a passenger from the Titanic</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">A recruit from the year 2150</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">She is the leader of The Order</button>
            </div>
            <div class="quiz-question">
                <p>3. What did The Monk do to the soldiers of The Order?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He shot them with a gun</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He ran away from them</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He raised his hands and stopped time</button>
            </div>
            <div class="quiz-question">
                <p>4. What was Jack's final decision?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He decided to return to his sad life in the city</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">He decided to stay in the Chronos Agency and protect the universe</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">He decided to join The Order</button>
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
            <a href="the_lost_boarding_pass.html" class="nav-btn">Next Story ➡</a>
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
                { id: '1', en: 'dangerously', es: 'peligrosamente' },
                { id: '2', en: 'timeline', es: 'línea de tiempo' },
                { id: '3', en: 'sadly', es: 'tristemente' },
                { id: '4', en: 'to destroy', es: 'destruir' },
                { id: '5', en: 'firmly', es: 'firmemente' },
                { id: '6', en: 'to bleed', es: 'sangrar' },
                { id: '7', en: 'if', es: 'si (condicional)' },
                { id: '8', en: 'forever', es: 'para siempre' }
            ];

            initMatchingGame('pre-vocab', storyVocabulary);
            initRecallTest('post-vocab', storyVocabulary);
        });
    </script>
</body>
</html>"""

with open("the_chronos_protocol_part3.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created the_chronos_protocol_part3.html")
