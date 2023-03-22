// WebSockets
let url = `ws://${window.location.host}/ws/admin-chat-panel/`

const chatSocket = new WebSocket(url)

chatSocket.onmessage = (e) => {
    let data = JSON.parse(e.data)
    console.log(data)
}