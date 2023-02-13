from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from apps.main.models import mainContactForm

# Create your views here.
def home(response):
    return render(response, 'main/static/home.html', {})

def contactFormPost(response):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        
        record = mainContactForm(name=name, email=email, text=text, verificated = False, texted_back = False)
        record.save()
    
    return redirect('')