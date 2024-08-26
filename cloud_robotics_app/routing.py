from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/(?P<robot_slug>\w+)/$', consumers.WebRobotConsumer.as_asgi()),
    # re_path(r'ws/tb3', consumers.WebRobotConsumer.as_asgi()),
]