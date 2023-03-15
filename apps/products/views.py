from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView, CreateView, View
from .models import MainCategory, Product, Opinions
from .forms import ProductAddForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import JsonResponse

# CRUD PRODUCT OPERATIONS
class ProductCreateView(CreateView):
    form_class = ProductAddForm
    template_name = 'products/static/product_add_form.html'
    success_url = '/products/create/product'

    def form_invalid(self, form):
        messages.error(self.request, 'Dane niepoprawne! Sprawdź poprawność danych!')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        form.instance.maincategory = MainCategory.objects.filter(id = 2).get()
        messages.success(self.request, 'Zapisano przedmiot!')
        return super().form_valid(form)
    
    def render_to_response(self, context, **response_kwargs):
        resp = super().render_to_response(context, **response_kwargs)
        if not context['form'].errors:
            resp['HX-Trigger'] = 'successRefresh'
        return resp

