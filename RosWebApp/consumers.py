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

    async def receive(self, text_data):

        data = json.loads(text_data)

        header = data['header']
        local_position = data['local_position']
        global_position = data['global_position']
        euler_orientation = data['euler_orientation']
        linear_velocity = data['linear_velocity']
        angular_velocity = data['angular_velocity']
        linear_acceleration = data['linear_acceleration']

        await self.channel_layer.group_send(
            self.robot_group_name,
            {
                'type': 'robot_data',
                'header': header,
                'local_position': local_position,
                'global_position': global_position,
                'euler_orientation': euler_orientation,
                'linear_velocity': linear_velocity,
                'angular_velocity': angular_velocity,
                'linear_acceleration': linear_acceleration
            }
        )
    
    async def robot_data(self, event):
        # send data to all clients in the group
        header = event['header']
        local_position = event['local_position']
        global_position = event['global_position']
        euler_orientation = event['euler_orientation']
        linear_velocity = event['linear_velocity']
        angular_velocity = event['angular_velocity']
        linear_acceleration = event['linear_acceleration']

        await self.send(text_data=json.dumps({
            'header': header,
            'local_position': local_position,
            'global_position': global_position,
            'euler_orientation': euler_orientation,
            'linear_velocity': linear_velocity,
            'angular_velocity': angular_velocity,
            'linear_acceleration': linear_acceleration
        }))