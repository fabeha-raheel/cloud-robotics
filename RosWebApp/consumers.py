import json
from typing import Any
from channels.generic.websocket import AsyncWebsocketConsumer

class WebRobotConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        robot_name = self.scope['url_route']['kwargs']['robot_name']
        self.group_name = f'{robot_name}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

    async def disconnect(self, code):
        
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        data = json.loads(text_data)

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'robot_data',
                'data': data
            }
        )

    async def robot_data(self, event):
        # This method handles messages received by the group.
        # It sends the data to all clients in the group.

        await self.send(text_data=json.dumps({event['data']}))
