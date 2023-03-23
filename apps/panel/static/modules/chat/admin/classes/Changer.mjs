// Class to dynamically change HTML
export class Changer{
    // // Required data
    // tiles -> dict of tiles' IDs in admin's chat panel
    // chatStats -> dict of stats' IDs in chat statistics
    constructor(tiles, chatStats){
        // Tiles IDs
        this.userChatsElem = document.querySelector(`#${tiles['userChats']}`)
        this.chatStatsElem = document.querySelector(`#${tiles['chatStats']}`)
        this.recentMessagesElem = document.querySelector(`#${tiles['recentMessages']}`)

        // Chat stats IDs
        this.STAT_clientMessagesElem = document.querySelector(`#${chatStats['clientMessagesNumber']}`)
        this.STAT_unreadClientMessagesElem = document.querySelector(`#${chatStats['unreadClientMessages']}`)
        this.STAT_staffMessagesElem = document.querySelector(`#${chatStats['staffMessages']}`)
        this.STAT_lastMessageDateElem = document.querySelector(`#${chatStats['lastMessage']}`)
        this.STAT_averageResponseTimeElem = document.querySelector(`#${chatStats['averageResponseTime']}`)
        this.STAT_numberOfTodayClientMessages = document.querySelector(`#${chatStats['todayClientMessages']}`)
        this.STAT_numberOfMonthClientMessages = document.querySelector(`#${chatStats['monthClientMessages']}`)
    }

    // Test Method to edit number of client messages
    increment_messages_from_clients(){
        let currentValue = parseInt(this.STAT_clientMessagesElem.textContent)
        currentValue++
        this.STAT_clientMessagesElem.textContent = currentValue
    }
}