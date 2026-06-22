document.addEventListener('DOMContentLoaded', () => {
    let tooltip = null;

    document.addEventListener('mouseup', handleSelection);
    document.addEventListener('touchend', handleSelection);

    // Hide tooltip on click outside
    document.addEventListener('mousedown', (e) => {
        if (tooltip && !tooltip.contains(e.target)) {
            removeTooltip();
        }
    });

    function handleSelection(e) {
        // If the user is clicking on the tooltip itself, don't interfere!
        if (tooltip && tooltip.contains(e.target)) {
            return;
        }

        // Slight delay to let the browser finish selection on touchend/mouseup
        setTimeout(() => {
            const selection = window.getSelection();
            const text = selection.toString().trim();

            if (!text || text.split(/\s+/).length > 4) {
                // If no text or more than 4 words, ignore to prevent cheating
                removeTooltip();
                return;
            }

            const range = selection.getRangeAt(0);
            const rect = range.getBoundingClientRect();

            // Don't show if the rect is invalid
            if (rect.width === 0 || rect.height === 0) return;

            showTooltip(text, rect);
        }, 150);
    }

    function showTooltip(text, rect) {
        removeTooltip();

        tooltip = document.createElement('div');
        tooltip.id = 'translator-tooltip';
        tooltip.innerHTML = `<span id="translate-btn">Translate 🌐</span>`;
        
        // Calculate position
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const scrollLeft = window.scrollX || document.documentElement.scrollLeft;
        
        // Place tooltip below the selected text to avoid overlapping with native mobile selection menus
        tooltip.style.top = `${rect.bottom + scrollTop + 15}px`;
        tooltip.style.left = `${rect.left + scrollLeft + (rect.width / 2)}px`;
        tooltip.style.transform = 'translateX(-50%)';

        document.body.appendChild(tooltip);

        const translateBtn = tooltip.querySelector('#translate-btn');
        translateBtn.addEventListener('click', async (e) => {
            e.stopPropagation();
            await performTranslation(text);
        });
    }

    function removeTooltip() {
        if (tooltip && tooltip.parentNode) {
            tooltip.parentNode.removeChild(tooltip);
            tooltip = null;
        }
    }

    async function performTranslation(text) {
        try {
            tooltip.innerHTML = 'Translating... ⏳';
            const res = await fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=en|es`);
            const data = await res.json();
            
            if (data && data.responseData && data.responseData.translatedText) {
                const translation = data.responseData.translatedText;
                
                // Show translation AND automatically save it
                tooltip.innerHTML = `<span style="color: #4ade80;">${translation} ✓</span>`;
                
                saveToVocabulary(text, translation);

            } else {
                tooltip.innerHTML = 'Error ❌';
            }
        } catch (error) {
            console.error('Translation error:', error);
            tooltip.innerHTML = 'Error ❌';
        }
    }

    function saveToVocabulary(enText, esText) {
        const vocab = JSON.parse(localStorage.getItem('myVocab') || '[]');
        
        // Avoid exact duplicates
        if (!vocab.find(v => v.en.toLowerCase() === enText.toLowerCase())) {
            vocab.push({
                en: enText,
                es: esText,
                date: Date.now()
            });
            localStorage.setItem('myVocab', JSON.stringify(vocab));
        }

        // Remove the browser text selection so it looks clean.
        // We leave the tooltip visible until the user clicks outside to close it.
        window.getSelection().removeAllRanges();
    }
});
