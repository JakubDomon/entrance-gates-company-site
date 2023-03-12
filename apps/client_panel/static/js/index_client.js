const button = document.querySelector('.button-click');

fetch('/auth/groups/')
    .then((response) => response.json())
    .then((data) => {
        button.innerHTML = data['Groups']['Staff']['name']
    })

button.addEventListener('click', (event) => {
    // Data values
    console.log('abcd');
    const data = {
        'group-id': 1,
        'users-id': [1, 2, 3, 4],
        'action': 'add_user_to_group',
    }

    var csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Send POST request to API
    fetch('/auth/groups/', {
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