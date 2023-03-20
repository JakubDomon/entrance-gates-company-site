from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, View, ListView
from apps.products.models import Product, MainCategory
from apps.products.forms import ProductForm, CategoryForm, ProductUpdateForm

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
    
