from channels import layers
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from django.core import serializers
from django.contrib.auth.models import User
import json

# Class to send events to WebSockets adminpanelroom -> default is set to send messages to 'adminpanelroom' group
class Notifier:
    def __init__(self, groupname: str='adminpanelroom', channellayer=layers.get_channel_layer()) -> None:
        self.group_name = groupname
        self.channel_layer = channellayer
        self.groups = ['Staff']

    def check_user_group(self, user, group):
            return user.groups.filter(name=group).exists()
    
    async def check_if_staff(self, user: object) -> bool:
        is_staff = False
        for group in self.groups:
            is_staff = await database_sync_to_async(self.check_user_group)(user=user, group=group)
        return is_staff

    def serialize_objects(self, objects: list) -> str:
        listToSerialize = list()
        if isinstance(objects, object): listToSerialize.append(objects)

        try: serialized_msg = serializers.serialize('json', listToSerialize)
        except: serialized_msg = ''

        # Add username field
        json_msg = json.loads(serialized_msg)
        json_msg[0]['fields']['user_name'] = objects.user.username
        serialized_msg = json.dumps(json_msg)

        return json.loads(serialized_msg)
    
    async def send_message_to_group(self, action: str, payload: json) -> None:
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'notify_event',
                'action': action,
                'payload': payload,
            }
        )

    def set_group_name(self, groupname:str) -> None:
        self.group_name = groupname
    
    def get_group_name(self) -> str:
        return self.group_name
    
class AdminChatPanelNotifier(Notifier):

    def __init__(self, groupname: str = 'adminpanelroom', channellayer=layers.get_channel_layer()) -> None:
        super().__init__(groupname, channellayer)
    
    async def notify_new_message_dashboard(self, messages: object, user: object) -> None:
        # Serialize objects
        serialized_payload = self.serialize_objects(messages)

        # Check if user has access to chat admin panel
        is_staff = await super().check_if_staff(user)

        # Define type of action
        if not is_staff: action = 'new_client_message'
        else: action = 'new_staff_message'

        # Send message to group
        await super().send_message_to_group(action, serialized_payload)

