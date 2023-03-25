// Import Changer class
import { Changer } from "./classes/Changer.mjs"

// WebSockets
let url = `ws://${window.location.host}/ws/admin-chat-panel/`
const chatSocket = new WebSocket(url)

// Changer
var tiles = {
    'userChats':'userChats',
    'chatStats':'chatStats',
    'recentMessages':'recentMessages'
}
var chatStats = {
    'clientMessagesNumber':'clientMessagesNumber',
    'unreadClientMessages':'unreadClientMessages',
    'staffMessages':'staffMessages',
    'lastMessage':'lastMessage',
    'averageResponseTime':'averageResponseTime',
    'todayClientMessages':'todayClientMessages',
    'monthClientMessages':'monthClientMessages'
}
const changer = new Changer(tiles, chatStats)

chatSocket.onmessage = (e) => {
    let data = JSON.parse(e.data)
    console.log(data)
    changer.increment_messages_from_clients()
    changer.increment_messages_from_clients_unread()
    changer.change_recent_client_message_date(data)
    changer.add_new_message(data)
}