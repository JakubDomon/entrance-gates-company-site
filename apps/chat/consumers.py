import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from .models import ChatRoom, Message
from django.core import serializers
from CustomClasses.WebSockets.Notifiers import AdminChatPanelNotifier

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['room']

        await self.channel_layer.group_add(
            str(self.room_group_name),
            self.channel_name
        )

        # Accept connection
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['user_name']
        user_id = text_data_json['user_id']
        
        # Save message to database
        room = await database_sync_to_async(ChatRoom.objects.get)(name=text_data_json['room'])
        msg = Message(text=message, user=self.scope['user'], chatroom=room)
        
        await database_sync_to_async(msg.save)()

        # Notify about new message
        notifier = AdminChatPanelNotifier()
        await notifier.notify_new_message_dashboard(msg, self.scope['user'])

        # Send message to group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
                'user_id':user_id,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        user_id = event['user_id']

        await self.send(text_data=json.dumps({
            'type':'chat',
            'message': message,
            'user_id': user_id,
            'user_name': username,
        }))