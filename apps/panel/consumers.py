from channels.generic.websocket import AsyncWebsocketConsumer
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