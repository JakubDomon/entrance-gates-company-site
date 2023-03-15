from django.urls import path

from . import views

urlpatterns = [
    path('products/create/product/', views.ProductCreateView.as_view(), name='create_product'),
]