import os
import json

chapters = [
    {
        "filename": "mere_christianity_b1_c2.html",
        "title": "Some Objections",
        "subtitle": "Mere Christianity (Book 1, Chapter 2) | Level: C1",
        "h2_title": "Is Morality Just an Instinct?",
        "text": """
            <p>If the Law of Human Nature is the foundation, I had better stop to make that foundation firm before I go on. A good many people find it difficult to understand just what this Law of Human Nature, or Moral Law, or Rule of Decent Behaviour is.</p>

            <p>For example, some people wrote to me saying, "Isn't what you call the Moral Law simply our herd <strong>instinct</strong> and hasn't it been developed just like all our other instincts?" Now I do not deny that we may have a herd instinct: but that is not what I mean by the Moral Law. We all know what it feels like to be <strong>prompted</strong> by instinct—by mother love, or sexual instinct, or the instinct for food. It means that you feel a strong want or desire to act in a certain way.</p>

            <p>But feeling a desire to help is quite different from feeling that you <em>ought</em> to help whether you want to or not. Supposing you hear a cry for help from a man in danger. You will probably feel two desires—one a desire to give help (due to your herd instinct), the other a desire to keep out of danger (due to the instinct for <strong>self-preservation</strong>). But you will find inside you, in addition to these two impulses, a third thing which tells you that you ought to follow the impulse to help, and <strong>suppress</strong> the impulse to run away.</p>

            <p>Now this thing that judges between two instincts, that decides which should be encouraged, cannot itself be either of them. You might as well say that the sheet of music which tells you, at a given moment, to play one note on the piano and not another, is itself one of the notes on the keyboard. The Moral Law tells us the tune we have to play: our instincts are merely the keys.</p>
            
            <p>Other people wrote to me saying, "Isn't what you call the Moral Law just a social <strong>convention</strong>, something that is put into us by education?" I fully agree that we learn the Rule of Decent Behaviour from parents and teachers. But some of the things we learn are mere conventions which might have been different—we learn to keep to the left of the road, but it might just as well have been the right—and others of them, like mathematics, are real truths. The question is to which class the Law of Human Nature belongs. I believe it belongs to the same class as mathematics.</p>
        """,
        "vocab": [
            {'id': '1', 'en': 'instinct', 'es': 'instinto'},
            {'id': '2', 'en': 'prompted', 'es': 'impulsado / motivado'},
            {'id': '3', 'en': 'self-preservation', 'es': 'autoconservación'},
            {'id': '4', 'en': 'suppress', 'es': 'reprimir / suprimir'},
            {'id': '5', 'en': 'convention', 'es': 'convención / costumbre'},
            {'id': '6', 'en': 'foundation', 'es': 'base / cimiento'},
            {'id': '7', 'en': 'herd', 'es': 'manada / rebaño'},
            {'id': '8', 'en': 'ought to', 'es': 'debería (obligación moral)'}
        ],
        "quiz": [
            ("What is the difference between an instinct and the Moral Law?", "Instincts are always bad, while the Moral Law is good", "An instinct is a desire, but the Moral Law tells you which desire you ought to follow", "They are exactly the same thing", 1),
            ("What analogy does Lewis use to explain the Moral Law?", "A teacher and a student", "A judge and a criminal", "A sheet of music and the keys of a piano", 2),
            ("Why does Lewis believe the Moral Law is not just a social convention?", "Because it is exactly the same in every single culture", "Because it is more like mathematics (a real truth) than like driving on the left side of the road", "Because nobody learns it from their parents", 1),
            ("When two instincts conflict (like helping vs. running away), what does the Moral Law usually tell us to do?", "It tells us to follow the strongest instinct", "It tells us to side with the weaker instinct to do the right thing", "It tells us to flip a coin", 1)
        ]
    },
    {
        "filename": "mere_christianity_b1_c3.html",
        "title": "The Reality of the Law",
        "subtitle": "Mere Christianity (Book 1, Chapter 3) | Level: C1",
        "h2_title": "The Peculiarity of Human Behaviour",
        "text": """
            <p>I now go back to what I said at the end of the first chapter, that there were two odd things about the human race. First, that they were <strong>haunted</strong> by the idea of a sort of behaviour they ought to practise, what you might call fair play, or <strong>decency</strong>, or morality, or the Law of Nature. Second, that they did not in fact do so.</p>

            <p>If you take a thing like a stone or a tree, it is what it is and there seems no sense in saying it ought to have been otherwise. Of course you may say a stone is 'the wrong shape' if you want to use it for a rockery, or that a tree is a bad tree because it does not give you as much shade as you expected. But all you mean is that the stone or the tree does not happen to be <strong>convenient</strong> for some purpose of your own. You are not, except as a joke, <strong>blaming</strong> them for that.</p>

            <p>It follows that what we usually call the laws of nature—the way weather works on a tree for example—may not really be laws in the strict sense, but only in a manner of speaking. When you say that falling stones always obey the law of gravitation, you only mean that, in fact, they do fall. You cannot be sure that there is anything over and above the facts themselves, any law about what <em>ought</em> to happen, as distinct from what <em>does</em> happen.</p>

            <p>But if you turn to the Law of Human Nature, it is a different matter. That law certainly does not mean 'what human beings, in fact, do'; for many of them do not obey this law at all, and none of them obey it completely. The law of gravity tells you what stones do if you drop them; but the Law of Human Nature tells you what human beings <em>ought</em> to do and do not.</p>
            
            <p>In other words, when you are dealing with humans, something else comes in above and beyond the actual facts. You have the facts (how men do behave) and you also have something else (how they ought to behave). The Moral Law, or Law of Human Nature, is not simply a fact about human behaviour. It must somehow or other be a real thing—a thing that is really there, not made up by ourselves.</p>
        """,
        "vocab": [
            {'id': '1', 'en': 'haunted', 'es': 'atormentado / perseguido (por una idea)'},
            {'id': '2', 'en': 'decency', 'es': 'decencia'},
            {'id': '3', 'en': 'convenient', 'es': 'conveniente / práctico'},
            {'id': '4', 'en': 'blaming', 'es': 'culpando'},
            {'id': '5', 'en': 'strict sense', 'es': 'sentido estricto'},
            {'id': '6', 'en': 'as distinct from', 'es': 'a diferencia de'},
            {'id': '7', 'en': 'peculiarity', 'es': 'peculiaridad / rareza'},
            {'id': '8', 'en': 'above and beyond', 'es': 'más allá de'}
        ],
        "quiz": [
            ("What does Lewis mean when he says a tree is 'bad'?", "That the tree has committed a moral sin", "That the tree does not suit human convenience or purposes", "That the tree is poisoned", 1),
            ("How is the Law of Human Nature different from the Law of Gravitation?", "The law of gravitation describes what happens, the moral law describes what ought to happen", "The law of human nature is easier to break", "The law of gravitation is a social convention", 0),
            ("According to the text, what are the two 'odd things' about humans?", "They sleep too much and eat too little", "They know they ought to behave in a certain way, but they fail to do so", "They build cities and fight wars", 1),
            ("Does Lewis think the Moral Law is just a human invention?", "Yes, he thinks it was made up by ancient philosophers", "No, he believes it is a real thing that exists beyond our actual behaviour", "He is not sure", 1)
        ]
    },
    {
        "filename": "mere_christianity_b1_c4.html",
        "title": "What Lies Behind the Law",
        "subtitle": "Mere Christianity (Book 1, Chapter 4) | Level: C1",
        "h2_title": "The Mind Behind the Universe",
        "text": """
            <p>Let us sum up what we have reached so far. The Law of Human Nature, or of Right and Wrong, must be something above and beyond the actual facts of human behaviour. In this case, besides the actual facts, you have something else—a real law which we did not invent and which we know we ought to obey.</p>

            <p>I now want to consider what this tells us about the universe we live in. Ever since men were able to think they have been wondering what this universe really is and how it came to be there. And, very roughly, two views have been held. First, there is what is called the <strong>materialist</strong> view. People who take that view think that matter and space just happen to exist, and always have existed, nobody knows why; and that the matter, behaving in certain fixed ways, has just happened, by a sort of <strong>fluke</strong>, to produce creatures like ourselves who are able to think.</p>

            <p>The other view is the <strong>religious</strong> view. According to it, what is behind the universe is more like a mind than it is like anything else we know. That is to say, it is conscious, and has purposes, and prefers one thing to another. And on this view it made the universe, partly for purposes we do not know, but partly, at any rate, in order to produce creatures like itself—I mean, like itself to the extent of having minds.</p>

            <p>You cannot find out which view is the right one by science in the ordinary sense. Science works by experiments. It watches how things behave. But why anything comes to be there at all, and whether there is anything behind the things science observes—something of a different kind—this is not a scientific question. The statement that there is any such thing, and the statement that there is no such thing, are neither of them statements that science can make.</p>
            
            <p>But there is one thing, and only one, in the whole universe which we know more about than we could learn from external observation. That one thing is Man. We do not merely observe men, we <em>are</em> men. In this case we have, so to speak, inside information; we are in the know. And because of that, we know that men find themselves under a moral law, which they did not make, and cannot quite forget even when they try. If there was a controlling power outside the universe, it could not show itself to us as one of the facts inside the universe. The only way in which we could expect it to show itself would be inside ourselves as an influence or a command trying to get us to behave in a certain way.</p>
        """,
        "vocab": [
            {'id': '1', 'en': 'fluke', 'es': 'casualidad / golpe de suerte'},
            {'id': '2', 'en': 'materialist', 'es': 'materialista'},
            {'id': '3', 'en': 'conscious', 'es': 'consciente'},
            {'id': '4', 'en': 'to the extent of', 'es': 'hasta el punto de'},
            {'id': '5', 'en': 'external observation', 'es': 'observación externa'},
            {'id': '6', 'en': 'in the know', 'es': 'al tanto / bien informado'},
            {'id': '7', 'en': 'controlling power', 'es': 'poder controlador'},
            {'id': '8', 'en': 'influence', 'es': 'influencia'}
        ],
        "quiz": [
            ("What is the 'materialist' view of the universe?", "That God created the universe using matter", "That matter and space just exist by chance and produced thinking creatures by a fluke", "That only spiritual things matter", 1),
            ("What is the 'religious' view?", "That the universe was made by something that resembles a conscious mind with purposes", "That religion should control science", "That humans are actually gods", 0),
            ("Why can't science answer whether there is a mind behind the universe?", "Because scientists are materialists", "Because science only observes how things behave, not why they exist", "Because science has already proven there is no God", 1),
            ("According to Lewis, what is the ONE thing in the universe we have 'inside information' about?", "The solar system", "Animals", "Human beings (Man)", 2)
        ]
    },
    {
        "filename": "mere_christianity_b1_c5.html",
        "title": "We Have Cause to be Uneasy",
        "subtitle": "Mere Christianity (Book 1, Chapter 5) | Level: C1",
        "h2_title": "The Terror and Comfort of Goodness",
        "text": """
            <p>I ended my last chapter with the idea that in the Moral Law somebody or something from beyond the material universe was actually getting at us. I expect when I reached that point some of you felt a certain <strong>annoyance</strong>. You may even have thought that I had played a trick on you—that I had been carefully wrapping up to look like philosophy what turns out to be one more religious sermon. You cannot put the clock back, you may say.</p>

            <p>But would you think I was joking if I said that you can put a clock back, and that if the clock is wrong it is often a very sensible thing to do? We all want progress. But progress means getting nearer to the place where you want to be. And if you have taken a wrong turning, then to go forward does not get you any nearer. If you are on the wrong road, progress means doing an <strong>about-turn</strong> and walking back to the right road.</p>

            <p>We are trying to see what we can find out about this Somebody on our own steam. We have two bits of evidence about the Somebody. One is the universe He has made. If we used that as our only clue, then I think we should have to conclude that He was a great artist (for the universe is a very beautiful place), but also that He is quite <strong>merciless</strong> and no friend to man (for the universe is a very dangerous and terrifying place). The other bit of evidence is that Moral Law which He has put into our minds.</p>

            <p>From this second bit of evidence we conclude that the Being behind the universe is intensely interested in right conduct—in fair play, unselfishness, courage, good faith, honesty and truthfulness. But there is nothing <strong>indulgent</strong> about the Moral Law. It is as hard as nails. It tells you to do the straight thing and it does not seem to care how painful, or dangerous, or difficult it is to do.</p>

            <p>If there does exist an absolute goodness it must hate most of what we do. This is the terrible <strong>fix</strong> we are in. If the universe is not governed by an absolute goodness, then all our efforts are in the long run hopeless. But if it is, then we are making ourselves enemies to that goodness every day. God is the only comfort, He is also the supreme terror: the thing we most need and the thing we most want to hide from. Christianity tells people to <strong>repent</strong> and promises them forgiveness. But it is after you have realized that there is a real Moral Law, and that you have broken it, that Christianity begins to talk. When you know you are sick, you will listen to the doctor.</p>
        """,
        "vocab": [
            {'id': '1', 'en': 'annoyance', 'es': 'molestia / irritación'},
            {'id': '2', 'en': 'about-turn', 'es': 'media vuelta'},
            {'id': '3', 'en': 'merciless', 'es': 'despiadado'},
            {'id': '4', 'en': 'indulgent', 'es': 'indulgente / permisivo'},
            {'id': '5', 'en': 'fix', 'es': 'aprieto / dilema'},
            {'id': '6', 'en': 'repent', 'es': 'arrepentirse'},
            {'id': '7', 'en': 'on our own steam', 'es': 'por nuestros propios medios'},
            {'id': '8', 'en': 'clue', 'es': 'pista'}
        ],
        "quiz": [
            ("What does Lewis say about 'putting the clock back'?", "It is impossible", "If the clock is wrong, it is the most sensible thing to do", "Only religious people want to go back in time", 1),
            ("What does the universe (as evidence) suggest about its creator?", "That He is an artist but also dangerous and merciless", "That He is weak", "That He loves humanity unconditionally", 0),
            ("Why is 'absolute goodness' described as a 'supreme terror'?", "Because absolute goodness must hate the bad things humans do every day", "Because goodness causes natural disasters", "Because goodness wants to destroy the universe", 0),
            ("When does Lewis say Christianity finally 'makes sense'?", "When you realize you are sick and need a doctor (forgiveness for breaking the law)", "When you have a perfect life", "When you stop believing in science", 0)
        ]
    }
]

def generate_html(chapter):
    quiz_html = ""
    for i, q in enumerate(chapter['quiz']):
        quiz_html += f'''
            <div class="quiz-question">
                <p>{i+1}. {q[0]}</p>
                <button class="quiz-btn" onclick="checkAnswer(this, {str(q[3]==0).lower()})">{q[1]}</button>
                <button class="quiz-btn" onclick="checkAnswer(this, {str(q[3]==1).lower()})">{q[2]}</button>
                <button class="quiz-btn" onclick="checkAnswer(this, {str(q[3]==2).lower()})">{q[3]}</button>
            </div>'''

    vocab_json = str(chapter['vocab']).replace("'", '"')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reading English - {chapter['title']}">
    <title>{chapter['title']} - Reading English</title>
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
        <div class="hero story-hero" style="background: linear-gradient(135deg, #0f172a, #334155);">
            <h1>{chapter['title']}</h1>
            <p>{chapter['subtitle']}</p>
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
            
            <h2>{chapter['h2_title']}</h2>
            
            {chapter['text']}
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

for chapter in chapters:
    with open(chapter['filename'], "w", encoding="utf-8") as f:
        f.write(generate_html(chapter))
    print(f"Created {chapter['filename']}")
