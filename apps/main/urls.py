from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('save/contact/', views.contactFormPost, name='saveContact'),
    path('save/opinions/', views.opinionFormPost, name='saveOpinions'),
    path('get/opinions/', views.opinionsGet, name='getOpinions'),
]