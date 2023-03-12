from django.urls import path
from . import views

urlpatterns = [
    path('staff/panel/', views.admin_panel, name='admin_panel'),
]