import json
from channels.generic.websocket import AsyncWebsocketConsumer

class UGVConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.group_name = 'ugv-tank'

        await self.channel_layer.group_add(
            self.group_name, 
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)

        if data['type'] == 'odom_data':

            odom_linear_x = data['data']['odom_linear_x']
            odom_linear_y = data['data']['odom_linear_y']
            odom_linear_z = data['data']['odom_linear_z']

            odom_angular_x = data['data']['odom_angular_x']
            odom_angular_y = data['data']['odom_angular_y']
            odom_angular_z = data['data']['odom_angular_z']
            odom_angular_w = data['data']['odom_angular_w']

            await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'odom_data',
                'odom_linear_x': odom_linear_x,
                'odom_linear_y': odom_linear_y,
                'odom_linear_z': odom_linear_z,
                'odom_angular_x': odom_angular_x,
                'odom_angular_y': odom_angular_y,
                'odom_angular_z': odom_angular_z,
                'odom_angular_w': odom_angular_w,
            })
        
        elif data['type'] == 'imu_data':

            imu_orient_x = data['data']['imu_orient_x']
            imu_orient_y = data['data']['imu_orient_y']
            imu_orient_z = data['data']['imu_orient_z']
            imu_orient_w = data['data']['imu_orient_w']

            imu_angVel_x = data['data']['imu_angVel_x']
            imu_angVel_y = data['data']['imu_angVel_y']
            imu_angVel_z = data['data']['imu_angVel_z']

            imu_linearAcc_x = data['data']['imu_linearAcc_x']
            imu_linearAcc_y = data['data']['imu_linearAcc_y']
            imu_linearAcc_z = data['data']['imu_linearAcc_z']

            await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'imu_data',
                'imu_orient_x': imu_orient_x,
                'imu_orient_y': imu_orient_y,
                'imu_orient_z': imu_orient_z,
                'imu_orient_w': imu_orient_w,
                'imu_angVel_x': imu_angVel_x,
                'imu_angVel_y': imu_angVel_y,
                'imu_angVel_z': imu_angVel_z,
                'imu_linearAcc_x': imu_linearAcc_x,
                'imu_linearAcc_y': imu_linearAcc_y,
                'imu_linearAcc_z': imu_linearAcc_z,
            })
        
        elif data['type'] == 'video_data':

            frame_data = data['data']['frame']  # Video frame data in base64 format

            await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'video_data',
                'frame': frame_data
            })
        
        elif data['type'] == 'cmd_vel':
            await self.send(text_data=json.dumps({'type': 'cmd_vel',
                'data': data['data']}))
            
            await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'cmd_vel',
                'data': data['data']
            })


    async def odom_data(self, event):
        # This method handles messages received by the group.
        # It sends the location data to all clients in the group.

        odom_linear_x = event['odom_linear_x']
        odom_linear_y = event['odom_linear_y']
        odom_linear_z = event['odom_linear_z']

        odom_angular_x = event['odom_angular_x']
        odom_angular_y = event['odom_angular_y']
        odom_angular_z = event['odom_angular_z']
        odom_angular_w = event['odom_angular_w']

        # Send the location data to the WebSocket as a text message
        await self.send(text_data=json.dumps({
                'type': 'odom_data',
                'odom_linear_x': odom_linear_x,
                'odom_linear_y': odom_linear_y,
                'odom_linear_z': odom_linear_z,
                'odom_angular_x': odom_angular_x,
                'odom_angular_y': odom_angular_y,
                'odom_angular_z': odom_angular_z,
                'odom_angular_w': odom_angular_w,
        }))

    async def imu_data(self, event):

        imu_orient_x = event['imu_orient_x']
        imu_orient_y = event['imu_orient_y']
        imu_orient_z = event['imu_orient_z']
        imu_orient_w = event['imu_orient_w']

        imu_angVel_x = event['imu_angVel_x']
        imu_angVel_y = event['imu_angVel_y']
        imu_angVel_z = event['imu_angVel_z']

        imu_linearAcc_x = event['imu_linearAcc_x']
        imu_linearAcc_y = event['imu_linearAcc_y']
        imu_linearAcc_z = event['imu_linearAcc_z']

        # Send the location data to the WebSocket as a text message
        await self.send(text_data=json.dumps({
                'type': 'imu_data',
                'imu_orient_x': imu_orient_x,
                'imu_orient_y': imu_orient_y,
                'imu_orient_z': imu_orient_z,
                'imu_orient_w': imu_orient_w,
                'imu_angVel_x': imu_angVel_x,
                'imu_angVel_y': imu_angVel_y,
                'imu_angVel_z': imu_angVel_z,
                'imu_linearAcc_x': imu_linearAcc_x,
                'imu_linearAcc_y': imu_linearAcc_y,
                'imu_linearAcc_z': imu_linearAcc_z,
        }))

    async def video_data(self, event):

        frame_data = event['frame']  # Video frame data in base64 format

        await self.send(text_data=json.dumps({
                'type': 'video_data',
                'frame': frame_data 
        }))

    async def cmd_vel(self, event):

        data = event['data']

        await self.send(text_data=json.dumps({
                'type': 'cmd_vel',
                'data': data 
        }))

class TB3Consumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.group_name = 'tb3'

        await self.channel_layer.group_add(
            self.group_name, 
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)

        if data['type'] == 'odom_data':

            odom_linear_x = data['data']['odom_linear_x']
            odom_linear_y = data['data']['odom_linear_y']
            odom_linear_z = data['data']['odom_linear_z']

            odom_angular_x = data['data']['odom_angular_x']
            odom_angular_y = data['data']['odom_angular_y']
            odom_angular_z = data['data']['odom_angular_z']
            odom_angular_w = data['data']['odom_angular_w']

            await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'odom_data',
                'odom_linear_x': odom_linear_x,
                'odom_linear_y': odom_linear_y,
                'odom_linear_z': odom_linear_z,
                'odom_angular_x': odom_angular_x,
                'odom_angular_y': odom_angular_y,
                'odom_angular_z': odom_angular_z,
                'odom_angular_w': odom_angular_w,
            })
        
        elif data['type'] == 'imu_data':

            imu_orient_x = data['data']['imu_orient_x']
            imu_orient_y = data['data']['imu_orient_y']
            imu_orient_z = data['data']['imu_orient_z']
            imu_orient_w = data['data']['imu_orient_w']

            imu_angVel_x = data['data']['imu_angVel_x']
            imu_angVel_y = data['data']['imu_angVel_y']
            imu_angVel_z = data['data']['imu_angVel_z']

            imu_linearAcc_x = data['data']['imu_linearAcc_x']
            imu_linearAcc_y = data['data']['imu_linearAcc_y']
            imu_linearAcc_z = data['data']['imu_linearAcc_z']

            await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'imu_data',
                'imu_orient_x': imu_orient_x,
                'imu_orient_y': imu_orient_y,
                'imu_orient_z': imu_orient_z,
                'imu_orient_w': imu_orient_w,
                'imu_angVel_x': imu_angVel_x,
                'imu_angVel_y': imu_angVel_y,
                'imu_angVel_z': imu_angVel_z,
                'imu_linearAcc_x': imu_linearAcc_x,
                'imu_linearAcc_y': imu_linearAcc_y,
                'imu_linearAcc_z': imu_linearAcc_z,
            })
        
        elif data['type'] == 'video_data':

            frame_data = data['data']['frame']  # Video frame data in base64 format

            await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'video_data',
                'frame': frame_data
            })
        
        elif data['type'] == 'cmd_vel':
            await self.send(text_data=json.dumps({'type': 'cmd_vel',
                'data': data['data']}))
            
            await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'cmd_vel',
                'data': data['data']
            })


    async def odom_data(self, event):
        # This method handles messages received by the group.
        # It sends the location data to all clients in the group.

        odom_linear_x = event['odom_linear_x']
        odom_linear_y = event['odom_linear_y']
        odom_linear_z = event['odom_linear_z']

        odom_angular_x = event['odom_angular_x']
        odom_angular_y = event['odom_angular_y']
        odom_angular_z = event['odom_angular_z']
        odom_angular_w = event['odom_angular_w']

        # Send the location data to the WebSocket as a text message
        await self.send(text_data=json.dumps({
                'type': 'odom_data',
                'odom_linear_x': odom_linear_x,
                'odom_linear_y': odom_linear_y,
                'odom_linear_z': odom_linear_z,
                'odom_angular_x': odom_angular_x,
                'odom_angular_y': odom_angular_y,
                'odom_angular_z': odom_angular_z,
                'odom_angular_w': odom_angular_w,
        }))

    async def imu_data(self, event):

        imu_orient_x = event['imu_orient_x']
        imu_orient_y = event['imu_orient_y']
        imu_orient_z = event['imu_orient_z']
        imu_orient_w = event['imu_orient_w']

        imu_angVel_x = event['imu_angVel_x']
        imu_angVel_y = event['imu_angVel_y']
        imu_angVel_z = event['imu_angVel_z']

        imu_linearAcc_x = event['imu_linearAcc_x']
        imu_linearAcc_y = event['imu_linearAcc_y']
        imu_linearAcc_z = event['imu_linearAcc_z']

        # Send the location data to the WebSocket as a text message
        await self.send(text_data=json.dumps({
                'type': 'imu_data',
                'imu_orient_x': imu_orient_x,
                'imu_orient_y': imu_orient_y,
                'imu_orient_z': imu_orient_z,
                'imu_orient_w': imu_orient_w,
                'imu_angVel_x': imu_angVel_x,
                'imu_angVel_y': imu_angVel_y,
                'imu_angVel_z': imu_angVel_z,
                'imu_linearAcc_x': imu_linearAcc_x,
                'imu_linearAcc_y': imu_linearAcc_y,
                'imu_linearAcc_z': imu_linearAcc_z,
        }))

    async def video_data(self, event):

        frame_data = event['frame']  # Video frame data in base64 format

        await self.send(text_data=json.dumps({
                'type': 'video_data',
                'frame': frame_data 
        }))

    async def cmd_vel(self, event):

        data = event['data']

        await self.send(text_data=json.dumps({
                'type': 'cmd_vel',
                'data': data 
        }))
