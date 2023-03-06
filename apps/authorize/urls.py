from django.urls import path
from . import views

urlpatterns = [
    path('auth/login/', views.login_user, name='login'),
    path('auth/register/', views.register, name='register'),
    path('auth/logout/', views.logout_user, name='logout'),
]
