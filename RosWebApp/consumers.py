import json

from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Robot

class WebRobotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.robot_slug = self.scope['url_route']['kwargs']['robot_slug']
        self.robot_group_name = f"{self.robot_slug}_group"

        await self.channel_layer.group_add(
            self.robot_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.robot_group_name,
            self.channel_name
        )