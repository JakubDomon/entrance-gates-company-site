// Import Changer class
import { Changer } from "./classes/Changer.mjs"
import { Router } from "./classes/Router.mjs"

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

// Router
const router = new Router(changer)

chatSocket.onmessage = (e) => {
    let message = JSON.parse(e.data)
    router.route(message)
}