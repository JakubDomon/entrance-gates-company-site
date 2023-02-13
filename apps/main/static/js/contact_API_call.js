// JS FILE TO CALL CONTACT API TO SAVE CONTACT DATA
const button = document.querySelector('.js-button');

const user_name = document.querySelector('.js-name');
const email = document.querySelector('.js-email');
const text = document.querySelector('.js-text');

const checkOptions = document.querySelectorAll('.js-name, .js-email, .js-text');

console.log(checkOptions)

checkOptions.forEach((elem) => {
    elem.addEventListener('keyup', () => {
        if(user_name.value.length >= 3 && email.value.includes('@') && text.value.length > 10){
            button.disabled = false;
        }else{
            button.disabled = true;
        }
    })
})


button.addEventListener('click', function(){
    // Data values
    const data = {
        'client-name': user_name.value,
        'client-email': email.value,
        'client-text': text.value,
    }

    var csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

    var csrf = 
    // Send POST request to API
    fetch('/save', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf,
        },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
        })
})