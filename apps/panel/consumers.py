from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels import layers
from asgiref.sync import async_to_sync
import json

class DashboardAdminConsumer(AsyncWebsocketConsumer):

    room_group_name = 'adminpanelroom'

    # Function to connect to room
    async def connect(self):
        # Join to group room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # Accept connection
        await self.accept()

    # Function to receive messages from WebSockets
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        payload = text_data_json['payload']

        # Send message to group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'notify_event',
                'action': action,
                'payload': payload,
            }
        )

    # Function to receive messages from room group
    async def notify_event(self, event):
        action = event['action']
        payload = event['payload']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'event',
            'action': action,
            'payload': payload,
        }))

def notify_chat_dashboard(action, payload):
    group_name = 'adminpanelroom'
    channel_layer = layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'notify_event',
            'action': action,
            'payload': payload
        }
    )