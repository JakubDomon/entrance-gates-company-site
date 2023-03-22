from django.urls import path

from . import views

urlpatterns = [
    # Products urls
    path('panel/products/', views.ProductViewList.as_view(), name='panelOrders'),
    # Chat urls
    path('panel/chat/', views.ChatLobbyViewList.as_view(), name='chat_lobby'),
    path('panel/chat/<str:room>', views.ChatRoomViewList.as_view(), name='chat_room'),
    path('panel/chat/admin/', views.ChatPanelAdminList.as_view(), name='admin_chat_panel'),
]