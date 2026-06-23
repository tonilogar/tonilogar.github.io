import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reading English - The Chronos Protocol: Part 1">
    <title>The Chronos Protocol: Part 1 - Reading English</title>
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
            <h1>The Chronos Protocol: Part 1</h1>
            <p>Level: A2+ | Epic Time Travel Adventure</p>
        </div>
    </header>

    <main class="content story-content">
        <section class="vocabulary">
            <h2>1. Match the Words (Pre-reading)</h2>
            <p style="margin-bottom: 1rem; color: #cbd5e1;">Click an English word, then click its Spanish translation. When you finish, the story will appear!</p>
            <div id="pre-vocab"></div>
        </section>

        <article class="story-text" style="display: none;" id="story-section">
            <div class="instruction-notice">
                💡 <strong>Tip:</strong> Double-click or select any word you don't know to translate and save it to <a href="my_vocabulary.html">My Vocabulary</a>!
            </div>
            
            <h2>The Recruitment</h2>
            
            <p>Jack was a detective. He worked in a very dark city. It rained every day, and the sky was always grey. He was sad. He didn't like his life. He sat in a bar every night and drank coffee.</p>
            
            <p>One day, he sat in his usual chair. The bar was empty. Suddenly, a strange man walked in. He wore simple, brown clothes. He looked very calm. In fact, he was the calmest man in the world. He walked slowly to Jack's table.</p>
            
            <p>"Are you Jack?" the man asked. His voice was soft.</p>
            
            <p>Jack looked at him. "Who are you?"</p>
            
            <p>"They call me The Monk," the man said. "I need your help."</p>
            
            <p>Jack laughed. "I don't help people anymore. I am retired."</p>
            
            <p>The Monk didn't smile. He didn't move. "This is more important than your sad life. We are going to save the universe."</p>
            
            <p>Suddenly, the bar disappeared. Everything was dark. Then, Jack saw a huge room. There were stars and galaxies everywhere. It was bigger than his city. It was the most beautiful place he ever saw.</p>
            
            <p>"Where are we?" Jack asked. He was afraid.</p>
            
            <p>"We are outside of time," The Monk said. "This is the Chronos Agency. We are the Keepers."</p>
            
            <p>"What do you keep?"</p>
            
            <p>"We keep the natural flow of time. The universe is wild. It is chaotic. It must be free."</p>
            
            <p>The Monk walked slowly. Jack followed him through the stars.</p>
            
            <p>"There is a group. They call themselves The Order," The Monk explained. "They are the worst people in history. They want to control everything. They want perfect order. They use time travel to change the past. If they change the past, they control the future."</p>
            
            <p>Jack listened carefully. "And you? Do you change the past?"</p>
            
            <p>"No. We protect it. Sometimes, bad things must happen. If we stop a tragedy, maybe we destroy the world. We are anarchists. We don't have leaders or presidents. We only listen to the universe."</p>
            
            <p>The Monk stopped in front of a long, silent hall. There were hundreds of statues made of stone.</p>
            
            <p>"Who are they?" Jack asked.</p>
            
            <p>"They are the Fallen Legends. They died in our missions. They died for the timeline."</p>
            
            <p>Jack looked at the statues. Some were old, some were young. They were braver than him.</p>
            
            <p>"We don't have an army," The Monk said. "We recruit normal people for specific missions. You are the best detective. You are the smartest man for this job."</p>
            
            <p>"What is the job?" Jack asked.</p>
            
            <p>"We are going to send you to the year 1912. The Order wants to stop a man. This man must board a ship. The ship is called the Titanic."</p>
            
            <p>Jack was shocked. "But the Titanic sank! A lot of people died!"</p>
            
            <p>"Yes," The Monk said. His voice was very quiet. "It was a terrible tragedy. But if that man does not board the ship, his grandson will be born. His grandson will become the leader of The Order. He will destroy freedom."</p>
            
            <p>Jack felt cold. "So... I must send a man to die?"</p>
            
            <p>"Yes. You must ensure he boards the ship. It is a very difficult choice. But it is necessary."</p>
            
            <p>"And after the mission? What happens to me?" Jack asked.</p>
            
            <p>"You are going to return to your bar. You will not remember me. You will not remember the agency. You will forget everything."</p>
            
            <p>Jack looked at the stars. He looked at the statues of the Fallen Legends. His life in the city was sad and boring. This was the most important thing in the world.</p>
            
            <p>He took a deep breath. He was ready.</p>
            
            <p>"Okay," Jack said. "I am going to help you. How do we travel to 1912?"</p>
            
            <p>The Monk finally smiled. "Close your eyes."</p>
        </article>

        <section class="quiz" style="display: none;" id="quiz-section">
            <h2>2. Comprehension Quiz (Cuestionario)</h2>
            <div class="quiz-question">
                <p>1. Where was Jack when he met The Monk?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">In a sunny park</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">In a dark bar</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">In a police station</button>
            </div>
            <div class="quiz-question">
                <p>2. Who are 'The Order'?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">A group that wants to control the past and the future</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">The people who built the statues</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">A group of anarchists</button>
            </div>
            <div class="quiz-question">
                <p>3. Why must the man board the Titanic?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because he is a bad person</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">Because if he lives, his grandson will destroy freedom</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">Because he wants to travel to America</button>
            </div>
            <div class="quiz-question">
                <p>4. What happens to the recruits after the mission?</p>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">They become statues</button>
                <button class="quiz-btn" onclick="checkAnswer(this, true)">They forget everything and return to their lives</button>
                <button class="quiz-btn" onclick="checkAnswer(this, false)">They stay in the Chronos Agency</button>
            </div>
        </section>

        <section class="vocabulary" style="display: none;" id="recall-section">
            <h2>3. Vocabulary Recall (Post-reading)</h2>
            <p style="margin-bottom: 1rem; color: #cbd5e1;">Test your memory. Type the translation in the box.</p>
            <div id="post-vocab"></div>
        </section>

        <div class="story-navigation" style="display: none;" id="nav-section">
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
                { id: '1', en: 'calm', es: 'tranquilo' },
                { id: '2', en: 'universe', es: 'universo' },
                { id: '3', en: 'flow', es: 'flujo' },
                { id: '4', en: 'freedom', es: 'libertad' },
                { id: '5', en: 'statues', es: 'estatuas' },
                { id: '6', en: 'tragedy', es: 'tragedia' },
                { id: '7', en: 'to remember', es: 'recordar' },
                { id: '8', en: 'to forget', es: 'olvidar' }
            ];

            initMatchingGame('pre-vocab', storyVocabulary);
            initRecallTest('post-vocab', storyVocabulary);
            
            // To reveal the story when matching is done:
            // The existing story.js logic reveals sections with class .story-text and .quiz
            // We'll let story.js handle it if it does, but just in case, we add an observer or check if the container has class 'completed'
            
            const observer = new MutationObserver((mutations) => {
                mutations.forEach((mutation) => {
                    if (mutation.target.classList.contains('completed')) {
                        document.getElementById('story-section').style.display = 'block';
                        document.getElementById('quiz-section').style.display = 'block';
                        document.getElementById('recall-section').style.display = 'block';
                        document.getElementById('nav-section').style.display = 'flex';
                    }
                });
            });
            
            const preVocab = document.getElementById('pre-vocab');
            if(preVocab) {
                observer.observe(preVocab, { attributes: true, attributeFilter: ['class'] });
            }
        });
    </script>
</body>
</html>"""

with open("the_chronos_protocol_part1.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Fixed the_chronos_protocol_part1.html")
