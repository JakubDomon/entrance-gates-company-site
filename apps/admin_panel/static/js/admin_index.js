const button = document.querySelector('.button-click');

button.addEventListener('click', (event) => {
    // Data values
    const data = {
        'group-name': 'abcdef',
        'description': 'assdfasdasdfasdffsd',
        'users': ['1','2'],
    }

    var csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Send POST request to API
    fetch('/auth/groups/create', {
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