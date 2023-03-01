// Scroll to contact section
const contactButton = document.querySelector('.scroll-btn');

console.log(contactButton);
contactButton.addEventListener('click', () => {
    console.log('juz');
    window.scrollTo(0, document.body.scrollHeight);
})