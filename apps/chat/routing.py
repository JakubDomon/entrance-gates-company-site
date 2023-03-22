from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/socket-server/<str:room>/', consumers.ChatConsumer.as_asgi(), name='consumer')
]