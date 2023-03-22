from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, View, ListView
from apps.products.models import Product, MainCategory
from apps.products.forms import ProductForm, CategoryForm, ProductUpdateForm
from apps.chat.models import Message, ChatRoom
from apps.chat.forms import MessageForm

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
class ChatLobbyViewList(ListView):
    model = Message
    context_object_name = 'chat_messages'
    template_name = 'panel/static/modules/chat/lobby.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messageForm'] = MessageForm
        return context
    
