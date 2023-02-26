from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save/contact/', views.contactFormPost, name='saveContact'),
    path('save/opinions/', views.opinionFormPost, name='saveOpinions'),
]