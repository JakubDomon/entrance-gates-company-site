// User id
const userID = JSON.parse(document.getElementById('user_id').textContent)
const userName = JSON.parse(document.getElementById('user_name').textContent)
console.log(userName)

// WebSockets
let chatName = window.location.pathname.replace('/panel/chat/', '')
let url = `ws://${window.location.host}/ws/socket-server/${chatName}/`

const chatSocket = new WebSocket(url)

// Construct message HTML body
var foreignMessage = (data) => {
    var message = `
        <div class="w-100 d-flex justify-content-start align-items-end flex-column">
            <div class="message-box d-flex justify-content-start align-items-end flex-column">
                <p class="p-0 m-1 ms-3 me-3 text-muted">${data.user_name}</p>
                <div class="w-100 border border-1 rounded-pill d-flex justify-content-start align-items-center mb-3" style="background-color: rgb(255, 255, 255);">
                    <p class="p-0 m-2 ms-3 me-3 text-break">${data.message}</p>
                </div>
            </div>
        </div>`

    return message
}

var userMessage = (data) => {
    var message = `
    <div class="w-100 d-flex justify-content-start flex-column">
            <div class="message-box d-flex justify-content-start flex-column">
                <p class="p-0 m-1 ms-3 me-3 text-muted">${data.user_name}</p>
                <div class="w-100 border border-1 rounded-pill d-flex justify-content-start align-items-center mb-3" style="background-color: rgb(255, 255, 255);">
                    <p class="p-0 m-2 ms-3 me-3 text-break">${data.message}</p>
                </div>
            </div>
    </div>`

    return message
}

chatSocket.onmessage = (e) => {
    let data = JSON.parse(e.data)
    console.log(data)

    if(data.type == 'chat'){
        if(data.user_id == userID){
            let messages = document.querySelector('#messages-place')
            messages.insertAdjacentHTML('afterbegin',userMessage(data))
        }else{
            let messages = document.querySelector('#messages-place')
            messages.insertAdjacentHTML('afterbegin',foreignMessage(data))
        }
    }
}
// Submit form on enter
let form = document.querySelector('#messageForm')

form.addEventListener('submit', (e)=>{
    e.preventDefault()
    let message = e.target.text.value
    console.log(message)
    chatSocket.send(JSON.stringify({
        'room': chatName,
        'message': message,
        'user_id':userID,
        'user_name':userName
    }))
    form.reset()
})