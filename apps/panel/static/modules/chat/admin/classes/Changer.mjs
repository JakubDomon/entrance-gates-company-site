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

    // STATS -> method to increment messages from clients
    increment_messages_from_clients(){
        // Increment message counter
        let currentValue = parseInt(this.STAT_clientMessagesElem.textContent)
        currentValue++
        this.STAT_clientMessagesElem.textContent = currentValue

        // Increment today messages
        let todayMessagesValue = parseInt(this.STAT_numberOfTodayClientMessages.textContent)
        todayMessagesValue++
        this.STAT_numberOfTodayClientMessages.textContent = todayMessagesValue

        // Increment value of month messages
        let monthMessagesValue = parseInt(this.STAT_numberOfMonthClientMessages.textContent)
        monthMessagesValue++
        this.STAT_numberOfMonthClientMessages.textContent = monthMessagesValue
    }

    // STATS -> method to increment unread messages from clients
    increment_messages_from_clients_unread(){
        let currentValue = parseInt(this.STAT_unreadClientMessagesElem.textContent)
        currentValue++
        this.STAT_unreadClientMessagesElem.textContent = currentValue
    }

    // STATS -> method to increment messages from staff
    increment_messages_from_staff(){
        let currentValue = parseInt(this.STAT_staffMessagesElem.textContent)
        currentValue++
        this.STAT_staffMessagesElem.textContent = currentValue
    }

    // STATS -> method to change date of last client message
    change_recent_client_message_date(message){
        let messageDateString = Date.parse(message.payload[0].fields.date)
        let messageDate = new Date(messageDateString)
        let day = ('0'+messageDate.getDate()).slice(-2)
        let month = ('0'+(messageDate.getMonth()+1)).slice(-2)
        let minutes = ('0'+messageDate.getMinutes()).slice(-2)
        let seconds = ('0'+messageDate.getSeconds()).slice(-2)
        let stringDate = `${messageDate.getFullYear()}-${month}-${day} ${messageDate.getHours()}:${minutes}:${seconds}`
        this.STAT_lastMessageDateElem.textContent = stringDate

        // Update date in chatroom
        let chatroomLastMessageElem = document.querySelector(`#chatroom-${message.payload[0].fields.chatroom}`)
        chatroomLastMessageElem.textContent = stringDate
    }

    change_recent_chatbox_message_date(message){
        let messageDateString = Date.parse(message.payload[0].fields.date)
        let messageDate = new Date(messageDateString)
        let day = ('0'+messageDate.getDate()).slice(-2)
        let month = ('0'+(messageDate.getMonth()+1)).slice(-2)
        let minutes = ('0'+messageDate.getMinutes()).slice(-2)
        let seconds = ('0'+messageDate.getSeconds()).slice(-2)
        let stringDate = `${messageDate.getFullYear()}-${month}-${day} ${messageDate.getHours()}:${minutes}:${seconds}`

        let chatroomLastMessageElem = document.querySelector(`#chatroom-${message.payload[0].fields.chatroom}`)
        chatroomLastMessageElem.textContent = stringDate
    }

    // STATS -> method to change average response delay
    //  TO DO

    // Message tile -> add new message
    add_new_message(message){
        // Construct string date
        let messageDateString = Date.parse(message.payload[0].fields.date)
        console.log(messageDateString)
        let messageDate = new Date(messageDateString)
        let day = ('0'+messageDate.getDate()).slice(-2)
        let month = ('0'+(messageDate.getMonth()+1)).slice(-2)
        let minutes = ('0'+messageDate.getMinutes()).slice(-2)
        let seconds = ('0'+messageDate.getSeconds()).slice(-2)
        let stringDate = `${messageDate.getFullYear()}-${month}-${day} ${messageDate.getHours()}:${minutes}:${seconds}`

        let messageHTML = `
            <tr id="${message.payload[0].pk}">
                <td>${message.payload[0].fields.user_name}</td>
                <td>${stringDate}</td>
                <td>${message.payload[0].fields.text}</td>
                <td><a href="/panel/chat/{{ message.chatroom.name }}"><i class="fa-solid fa-message"></i></a></td>
            </tr>`
        
        this.recentMessagesElem.insertAdjacentHTML('afterbegin', messageHTML)
    }
    
}