from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from apps.main.models import MainContactForm, MainCategory, Subcategory, Product, Opinions, CompanyOpinions
import json

# Create your views here.
def home(request):
    # Getting products
    return render(request, 'main/static/home.html', {})

# VIEW TO SAVE CONTACT MESSAGE TO DATABASE
def contactFormPost(request):
    if request.method == 'POST':
        # Get data from request
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data['client-name']
            email = data['client-email']
            text = data['client-text']
        except:
            response = {
                'message': 'Nie zapisano wiadomości! Niepoprawne dane',
                'status': 'error',
            }
            return JsonResponse(response, safe=False)

        # Check if input data is incorrect
        if((len(name) < 3) or ('@' not in email) or (len(text) < 10)):
            response = {
                'message': 'Nie zapisano wiadomości! Niepoprawne dane',
                'status': 'error',
            }
            return JsonResponse(response, safe=False)

        # If data is correct - save to database
        record = MainContactForm(name=name, email=email, text=text, verificated = False, texted_back = False)
        record.save()

        response = {
            'message': 'Zapisano wiadomość',
            'status': 'success',
        }
        return JsonResponse(response, safe=False)

    return redirect('/')

def opinionFormPost(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data['opinion-name']
            text = data['opinion-text']
        except:
            response = {
                'message': 'Nie zapisano opinii! Niepoprawne dane',
                'status': 'error',
                }
            return JsonResponse(response, safe=False)
        
        nameLen = len(name)
        if((nameLen == 0 or nameLen > 50) and len(text) < 5):
            response = {
                'message': 'Nie zapisano opinii! Niepoprawne dane',
                'status': 'error',
            }
        
        record = CompanyOpinions(author=name, text=text)
        record.save()

        response = {
            'message': 'Zapisano opinię!',
            'status': 'success',
        }
        return JsonResponse(response, safe=False)

    return redirect('/')