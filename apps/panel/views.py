from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, View, ListView
from apps.products.models import Product, MainCategory
from apps.products.forms import ProductForm, CategoryForm

# Create your views here.
class ProductViewList(ListView):
    model = MainCategory
    context_object_name = 'categories'
    template_name = 'panel/static/modules/products/products.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productForm'] = ProductForm
        context['categoryForm'] = CategoryForm
        return context
    
