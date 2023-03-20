from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView, CreateView, View
from .models import MainCategory, Product, Opinions
from .forms import ProductForm, CategoryForm, ProductUpdateForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse

# CRUD PRODUCT OPERATIONS
class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'products/static/product/product_create.html'
    success_url = '/products/create/product/'
    
    def form_invalid(self, form):
        messages.error(self.request, 'Dane niepoprawne! Sprawdź poprawność danych!')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        form.instance.maincategory = MainCategory.objects.filter(id = self.kwargs['maincategory']).get()
        form.instance.added_by = self.request.user
        messages.success(self.request, 'Zapisano przedmiot!')
        return super().form_valid(form)

    def get_success_url(self):
        url = super().get_success_url()
        url += self.kwargs['maincategory']
        return url
    
    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        if 'success' in response.rendered_content:
            response['HX-Trigger'] = 'refreshPage'
        return response
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/static/product/product_delete.html'
    success_url = '/panel/products'
    
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    success_url = '/products/update/product/'
    template_name = 'products/static/product/product_update.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Dane niepoprawne! Sprawdź poprawność danych!')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'Zapisano zmiany w przedmiocie!')
        return super(ProductUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        url = super().get_success_url()
        url += self.kwargs['pk']
        return url
    
    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        if 'success' in response.rendered_content:
            response['HX-Trigger'] = 'refreshPage'
        return response
    
# CRUD CATEGORY OPERATIONS
class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'products/static/category/category_create.html'
    success_url = '/products/create/category'
    
    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        if 'success' in response.rendered_content:
            response['HX-Trigger'] = 'refreshPage'
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Dane niepoprawne! Sprawdź poprawność danych!')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        messages.success(self.request, 'Zapisano kategorię!')
        return super().form_valid(form)

class CategoryDeleteView(DeleteView):
    model = MainCategory
    template_name = 'products/static/category/category_delete.html'
    success_url = '/panel/products'

class CategoryUpdateView(UpdateView):
    model = MainCategory
    form_class = CategoryForm
    success_url = '/products/update/category/'
    template_name = 'products/static/category/category_update.html'
    
    def get_success_url(self):
        url = super().get_success_url()
        url += self.kwargs['pk']
        return url

    def form_invalid(self, form):
        messages.error(self.request, 'Dane niepoprawne! Sprawdź poprawność danych!')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'Zapisano zmiany w kategorii!')
        return super().form_valid(form)
    
    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        if 'success' in response.rendered_content:
            response['HX-Trigger'] = 'refreshPage'
        return response