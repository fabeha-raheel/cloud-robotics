from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/tb3', consumers.TB3Consumer.as_asgi()),
#     re_path(r'ws/ugv', consumers.WebRobotConsumer.as_asgi()),
#     # re_path(r'ws/uav', consumers.UAVConsumer.as_asgi()),
# ]

websocket_urlpatterns = [
    re_path(r'ws/(?P<robot_name>\w+)/webrobot/$', consumers.WebRobotConsumer.as_asgi()),
]