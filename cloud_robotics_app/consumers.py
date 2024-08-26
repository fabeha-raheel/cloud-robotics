# consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Robot


class WebRobotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.robot_slug = self.scope['url_route']['kwargs']['robot_slug']
        # self.robot_group_name = f"{self.robot_slug}_group"

        self.robot_group_name = "tb3"

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

        if data['cmdtype'] == 'tb3data':
            header = data['data']['header']
            local_position = data['data']['local_position']
            global_position = data['data']['global_position']
            euler_orientation = data['data']['euler_orientation']
            linear_velocity = data['data']['linear_velocity']
            angular_velocity = data['data']['angular_velocity']
            linear_acceleration = data['data']['linear_acceleration']
            video = data['data']['video']

            await self.channel_layer.group_send(
            self.robot_group_name,
            {
                'type': 'robotdata',
                'cmdtype': 'tb3data',
                'header': header,
                'local_position': local_position,
                'global_position': global_position,
                'euler_orientation': euler_orientation,
                'linear_velocity': linear_velocity,
                'angular_velocity': angular_velocity,
                'linear_acceleration': linear_acceleration,
                'video': video,
            }
            )
        elif data['cmdtype'] == 'cmd_vel':
            print("Received cmd_vel data")
            print(data)
            await self.send(text_data=json.dumps({'type': 'cmd_vel',
                'data': data['data']}))
            
            await self.channel_layer.group_send(
            self.robot_group_name,
            {
                'type': 'cmd_handler',
                'cmdtype': 'cmd_vel',
                'data': data['data'],
            })
    
    async def robotdata(self, event):
        # send data to all clients in the group
        header = event['header']
        local_position = event['local_position']
        global_position = event['global_position']
        euler_orientation = event['euler_orientation']
        linear_velocity = event['linear_velocity']
        angular_velocity = event['angular_velocity']
        linear_acceleration = event['linear_acceleration']
        video = event['video']

        await self.send(text_data=json.dumps({
            'cmdtype': 'tb3data',
            'header': header,
            'local_position': local_position,
            'global_position': global_position,
            'euler_orientation': euler_orientation,
            'linear_velocity': linear_velocity,
            'angular_velocity': angular_velocity,
            'linear_acceleration': linear_acceleration,
            'video': video,
        }))

    async def cmd_handler(self, event):

        data = event['data']

        await self.send(text_data=json.dumps({
                'cmdtype': 'cmd_vel',
                'data': data 
        }))
