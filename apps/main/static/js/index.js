// Scroll to products
const arrowDiv = document.querySelector('.btn-arrow-js');
const newProductsDiv = document.querySelector('.new-products');

arrowDiv.addEventListener('click', (e) => {
    e.preventDefault();
    newProductsDiv.scrollIntoView({behavior:'smooth', block:'center', inline:'center'});
})

// Delete message after 4 seconds
const messageDiv = document.querySelector('.message-div');
const deleteTime = 3000;

setTimeout(()=>{
    messageDiv.classList.add('fadeOut');
}, deleteTime);