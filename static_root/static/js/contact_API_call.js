// JS FILE TO CALL CONTACT API TO SAVE CONTACT DATA
const button = document.querySelector('.js-button');

const user_name = document.querySelector('.js-name');
const email = document.querySelector('.js-email');
const text = document.querySelector('.js-text');

const checkOptions = document.querySelectorAll('.js-name, .js-email, .js-text');

console.log(checkOptions)

checkOptions.forEach((elem) => {
    elem.addEventListener('keyup', () => {
        if(user_name.value.length >= 3 && email.value.includes('@') && text.value.length > 5){
            button.disabled = false;
        }else{
            button.disabled = true;
        }
    })
})


button.addEventListener('click', function(){
    console.log('abcd');
    console.log(user_name.value.length);
})