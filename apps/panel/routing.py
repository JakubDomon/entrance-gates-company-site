from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/admin-chat-panel/', consumers.DashboardAdminConsumer.as_asgi(), name='dashboardChatConsumer')
]