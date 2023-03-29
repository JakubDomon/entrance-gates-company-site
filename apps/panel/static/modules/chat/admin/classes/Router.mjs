// Class to route message actions
export class Router{
    constructor(changer){
        this.changer = changer
    }

    // Method to route actions
    route(message){
        console.log(message)
        switch(message.action){
            case 'new_client_message':
                // Increment client messages counter
                this.changer.increment_messages_from_clients()
                // Change recent client message date
                this.changer.change_recent_client_message_date(message)
            
            case 'new_staff_message':
                // Increment messages from staff counter
                this.changer.increment_messages_from_staff()
                this.changer.change_recent_chatbox_message_date(message)
            
            case 'new_event_from_server':
                console.log('toDO')
        }
    }
}