import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import ChatRoom, Message

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['room']

        async_to_sync(self.channel_layer.group_add)(
            str(self.room_group_name),
            self.channel_name
        )

        # Accept connection
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['user_name']
        user_id = text_data_json['user_id']
        
        # Save message to database
        room = ChatRoom.objects.filter(name=text_data_json['room']).get()
        msg = Message(text=message, user=self.scope['user'], chatroom=room)
        msg.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
                'user_id':user_id,
            }
        )

    def chat_message(self, event):
        message = event['message']
        username = event['username']
        user_id = event['user_id']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message': message,
            'user_id': user_id,
            'user_name': username,
        }))