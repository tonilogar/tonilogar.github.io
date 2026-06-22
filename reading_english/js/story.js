function checkAnswer(btn, isCorrect) {
    const parent = btn.parentElement;
    const buttons = parent.querySelectorAll('.quiz-btn');
    
    // Disable all buttons in this question
    buttons.forEach(b => {
        b.disabled = true;
        b.style.cursor = 'default';
    });

    if (isCorrect) {
        btn.classList.add('correct');
        btn.innerHTML += ' ✓';
    } else {
        btn.classList.add('incorrect');
        btn.innerHTML += ' ✗';
        
        // Highlight the correct answer
        buttons.forEach(b => {
            if (b.getAttribute('onclick').includes('true')) {
                b.classList.add('correct');
            }
        });
    }
}

/* --- Pre-reading Matching Game --- */
function initMatchingGame(containerId, words) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Separate English and Spanish words and shuffle them independently
    const enWords = words.map(w => ({ id: w.id, text: w.en }));
    const esWords = words.map(w => ({ id: w.id, text: w.es }));

    // Fisher-Yates shuffle
    const shuffle = array => {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    };

    shuffle(enWords);
    shuffle(esWords);

    let html = '<div class="matching-game-container">';
    
    // English Column
    html += '<div class="match-column">';
    enWords.forEach(w => {
        html += `<button class="match-btn en-btn" data-id="${w.id}">${w.text}</button>`;
    });
    html += '</div>';

    // Spanish Column
    html += '<div class="match-column">';
    esWords.forEach(w => {
        html += `<button class="match-btn es-btn" data-id="${w.id}">${w.text}</button>`;
    });
    html += '</div></div>';

    container.innerHTML = html;

    let selectedEn = null;
    let selectedEs = null;
    let matchesFound = 0;

    const enBtns = container.querySelectorAll('.en-btn');
    const esBtns = container.querySelectorAll('.es-btn');

    enBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (btn.classList.contains('matched')) return;
            enBtns.forEach(b => b.classList.remove('selected'));
            btn.classList.add('selected');
            selectedEn = btn;
            checkMatch();
        });
    });

    esBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (btn.classList.contains('matched')) return;
            esBtns.forEach(b => b.classList.remove('selected'));
            btn.classList.add('selected');
            selectedEs = btn;
            checkMatch();
        });
    });

    function checkMatch() {
        if (selectedEn && selectedEs) {
            const idEn = selectedEn.getAttribute('data-id');
            const idEs = selectedEs.getAttribute('data-id');

            if (idEn === idEs) {
                // Correct match
                selectedEn.classList.remove('selected');
                selectedEs.classList.remove('selected');
                selectedEn.classList.add('matched');
                selectedEs.classList.add('matched');
                selectedEn.innerHTML += ' ✓';
                selectedEs.innerHTML += ' ✓';
                selectedEn = null;
                selectedEs = null;
                matchesFound++;
                if (matchesFound === words.length) {
                    setTimeout(() => alert('Great job! You can now read the story.'), 300);
                }
            } else {
                // Wrong match
                const tempEn = selectedEn;
                const tempEs = selectedEs;
                tempEn.classList.add('error');
                tempEs.classList.add('error');
                
                setTimeout(() => {
                    tempEn.classList.remove('error', 'selected');
                    tempEs.classList.remove('error', 'selected');
                }, 400);

                selectedEn = null;
                selectedEs = null;
            }
        }
    }
}

/* --- Post-reading Recall Test --- */
function initRecallTest(containerId, words) {
    const container = document.getElementById(containerId);
    if (!container) return;

    let targetLanguage = 'es'; // 'es' or 'en' (what the user has to type)

    function render() {
        let html = `
            <div class="recall-controls">
                <button class="recall-toggle-btn" id="toggleLangBtn">
                    Mode: Translate to ${targetLanguage === 'es' ? 'Spanish' : 'English'} 🔄
                </button>
            </div>
            <div class="recall-list">
        `;

        words.forEach(w => {
            const displayWord = targetLanguage === 'es' ? w.en : w.es;
            const targetWord = targetLanguage === 'es' ? w.es : w.en;
            
            html += `
                <div class="recall-item">
                    <div class="recall-word">${displayWord}</div>
                    <div class="recall-input-container">
                        <input type="text" class="recall-input" data-answer="${targetWord}" placeholder="Type translation...">
                        <button class="recall-hint-btn" title="Show hint">👁</button>
                        <button class="recall-check-btn" title="Check">Check</button>
                    </div>
                </div>
            `;
        });

        html += '</div>';
        container.innerHTML = html;
        attachEvents();
    }

    // Helper to normalize strings: lowercase, remove accents, trim
    const normalize = str => {
        return str.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim();
    };

    function attachEvents() {
        document.getElementById('toggleLangBtn').addEventListener('click', () => {
            targetLanguage = targetLanguage === 'es' ? 'en' : 'es';
            render();
        });

        const items = container.querySelectorAll('.recall-item');
        items.forEach(item => {
            const input = item.querySelector('.recall-input');
            const checkBtn = item.querySelector('.recall-check-btn');
            const hintBtn = item.querySelector('.recall-hint-btn');

            const verifyAnswer = () => {
                const answer = input.getAttribute('data-answer');
                // Support multiple answers if separated by '/'
                const possibleAnswers = answer.split('/').map(ans => normalize(ans));
                const userAnswer = normalize(input.value);

                input.classList.remove('correct', 'incorrect');
                if (userAnswer === '') return;

                if (possibleAnswers.includes(userAnswer)) {
                    input.classList.add('correct');
                    checkBtn.classList.add('correct');
                    checkBtn.innerHTML = '✓';
                    input.disabled = true;
                    checkBtn.disabled = true;
                    hintBtn.disabled = true;
                } else {
                    input.classList.add('incorrect');
                }
            };

            checkBtn.addEventListener('click', verifyAnswer);
            input.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') verifyAnswer();
            });

            hintBtn.addEventListener('click', () => {
                input.value = input.getAttribute('data-answer').split('/')[0];
                verifyAnswer();
            });
        });
    }

    render();
}
