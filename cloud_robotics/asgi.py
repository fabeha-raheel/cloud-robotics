"""
ASGI config for cloud_robotics project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import cloud_robotics_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloud_robotics.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                cloud_robotics_app.routing.websocket_urlpatterns
            )
        )
    }
)
