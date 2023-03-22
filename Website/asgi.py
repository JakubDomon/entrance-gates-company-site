"""
ASGI config for Website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import apps.chat.routing as chat
import apps.panel.routing as adminChatDashboard

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Website.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(adminChatDashboard.websocket_urlpatterns + chat.websocket_urlpatterns
        )
    )
})
