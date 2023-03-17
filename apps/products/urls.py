from django.urls import path

from . import views

urlpatterns = [
    path('products/create/product/<maincategory>', views.ProductCreateView.as_view(), name='create_product'),
    path('products/delete/product/<pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('products/update/product/<pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('products/create/category/', views.CategoryCreateView.as_view(), name='create_category'),
    path('products/delete/category/<pk>/', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('products/update/category/<pk>/', views.CategoryUpdateView.as_view(), name='update_category'),
]