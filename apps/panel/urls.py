from django.urls import path

from . import views

urlpatterns = [
    path('panel/products/', views.ProductViewList.as_view(), name='panelOrders'),
    path('panel/chat/', views.ChatLobbyViewList.as_view(), name='chat_lobby')
]