document.addEventListener('DOMContentLoaded', () => {
    // Add interactivity for the CTA button
    const startBtn = document.getElementById('startBtn');
    
    if (startBtn) {
        startBtn.addEventListener('click', () => {
            // Smooth scroll to lessons section
            const lessonsSection = document.getElementById('lessons');
            if (lessonsSection) {
                lessonsSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }

    // Add subtle reveal animations for lesson cards
    const cards = document.querySelectorAll('.lesson-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    cards.forEach((card, index) => {
        // Set initial state
        card.style.opacity = 0;
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.5s ease ${index * 0.1}s, transform 0.5s ease ${index * 0.1}s`;
        
        observer.observe(card);
    });
});
