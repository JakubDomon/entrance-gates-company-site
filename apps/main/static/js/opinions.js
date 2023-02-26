// Loading opinions from database
// DO UZUPEŁNIENIA !!!

// Opinion form 
const opinionBtn = document.querySelector('.opinion-button');
const opinionsForm = document.querySelector('.opinions-form');
const formOpinionsUsr = document.querySelector('.opinions-form-user');

opinionBtn.addEventListener('click', (event) =>{
    opinionsForm.style.background = 'none';
    make_visible(formOpinionsUsr);
})

const opinionName = document.querySelector('.js-opinion-name');
const opinionText = document.querySelector('.js-opinion-text');
const opinionSubmitButton = document.querySelector('.opinion-btn-js');

forms = [opinionName, opinionText];

forms.forEach(element => {
    element.addEventListener('keyup', () => {
        if(opinionName.value.length != 0 && opinionText.value.length > 5){
            opinionSubmitButton.disabled = false;
        }else{
            opinionSubmitButton.disabled = true;
        }
    })
});



opinionSubmitButton.addEventListener('click', function(){
    // Data values
    const data = {
        'opinion-name': opinionName.value,
        'opinion-text': opinionText.value,
    }

    var csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Send POST request to API
    fetch('save/opinions/', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf,
        },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((data) => {
            if(data['status'] == 'success'){
                show_message(opinionsForm, data['message'])
                setTimeout(() => {
                    opinionsForm.replaceChildren('');
                    opinionsForm.style.backgroundImage = "url('../images/opinions.png')";
                }, 4000)
            }
        })
})

function make_visible(element){
    element.style.visibility = 'visible';
}

function make_hidden(element){
    element.style.visibility = 'hidden';
}

function show_message(elementToAppend, text){
    let border = document.createElement('div');
    border.classList.add('border-opinion', 'd-flex', 'justify-content-center', 'align-items-center');

    let textDiv = document.createTextNode(text);
    
    border.appendChild(textDiv);

    elementToAppend.replaceChildren(border);
}