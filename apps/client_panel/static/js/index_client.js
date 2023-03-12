const button = document.querySelector('.button-click');

fetch('/auth/groups/')
    .then((response) => response.json())
    .then((data) => {
        console.log(data)
    })

button.addEventListener('click', (event) => {
    // Data values
    console.log('abcd');
    const data = {
        'group-name': 'Staff',
        'permissions': ['add_group', 'change_group', 'delete_group', 'view_group'],
        'users': [1, 2],
        'action': 'add_group',
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