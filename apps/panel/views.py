from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import FormView, View, ListView, RedirectView
from apps.products.models import Product, MainCategory
from apps.products.forms import ProductForm, CategoryForm, ProductUpdateForm
from apps.chat.models import Message, ChatRoom
from apps.chat.forms import MessageForm
import random, string
from django.db.models import Q
from functools import reduce
from operator import or_

# Views for admin panel
class ProductViewList(ListView):
    model = MainCategory
    context_object_name = 'categories'
    template_name = 'panel/static/modules/products/products_admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productForm'] = ProductForm
        context['productUpdateForm'] = ProductUpdateForm
        context['categoryForm'] = CategoryForm
        return context
    
# Views for chat
class ChatLobbyViewList(RedirectView):
    url = '/panel/chat/'
    
    def get_redirect_url(self, *args, **kwargs):
        redirectUrl = super().get_redirect_url(*args, **kwargs)
        # Get user ChatRoom
        if not self.request.user.groups.filter(name='Staff').exists():
            if ChatRoom.objects.filter(createdBy=self.request.user).exists():
                chatrooms = ChatRoom.objects.filter(createdBy=self.request.user).last()
                userChat = chatrooms.name
            else:
                userChat = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
                # Create ChatRoom
                chatroom = ChatRoom(name=userChat, createdBy=self.request.user)
                chatroom.save()
            
            # Append chat name to URL
            redirectUrl += userChat
        else:
            redirectUrl += 'admin/'

        return redirectUrl

# Client chat room
class ChatRoomViewList(ListView):
    model = Message
    context_object_name = 'chat_messages'
    template_name = 'panel/static/modules/chat/room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messageForm'] = MessageForm
        return context
    
    def get_queryset(self):
        chatroom = ChatRoom.objects.filter(name=self.kwargs['room']).get()
        queryset = Message.objects.filter(chatroom=chatroom.id).order_by('-date')
        return queryset
    
class ChatPanelAdminList(ListView):
    model = ChatRoom
    context_object_name = 'chat_rooms'
    template_name = 'panel/static/modules/chat/admin/panel.html'

    def get_queryset(self):
        chatrooms = ChatRoom.objects.exclude(message=None)
        return chatrooms
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get users
        users = User.objects.filter(groups__name='Staff')
        userConditions = reduce(or_, (Q(user=usr) for usr in users))
        context['lastMessages'] = Message.objects.exclude(userConditions).order_by('-date')
        return context