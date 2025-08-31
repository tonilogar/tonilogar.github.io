// Año en footer
document.getElementById('year').textContent = new Date().getFullYear();

// Filtro por texto
const search = document.getElementById('search');
const cards = Array.from(document.querySelectorAll('.card'));

function filterCards() {
  const q = (search.value || '').toLowerCase();
  cards.forEach(card => {
    const txt = card.textContent.toLowerCase();
    card.style.display = txt.includes(q) ? '' : 'none';
  });
}
search.addEventListener('input', filterCards);
