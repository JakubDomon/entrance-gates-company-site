from django.urls import path

from . import views

urlpatterns = [
    path('panel/products/', views.ProductViewList.as_view(), name='panelOrders'),
]