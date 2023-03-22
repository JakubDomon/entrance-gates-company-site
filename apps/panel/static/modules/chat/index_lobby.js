// WebSockets
let url = `ws://${window.location.host}/ws/socket-server/`

const chatSocket = new WebSocket(url)

// Construct message body
var message = (message) => {
    var messageWrapper = document.createElement('div')
    messageWrapper.classList.add('w-100', 'd-flex', 'justify-content-start')
    
    var messagePayload = document.createElement('p')
    messagePayload.innerText = message

    var messageBody = messageWrapper.appendChild(messagePayload)

    return messageBody
}

chatSocket.onmessage = (e) => {
    let data = JSON.parse(e.data)
    console.log(data)

    if(data.type == 'chat'){
        let messages = document.querySelector('#messages-place')
        messages.insertAdjacentElement('afterend', message(data.message))
    }
}

let form = document.querySelector('#messageForm')
form.addEventListener('submit', (e)=>{
    e.preventDefault()
    let message = e.target.text.value
    console.log(message)
    chatSocket.send(JSON.stringify({
        'message': message
    }))
    form.reset()
})