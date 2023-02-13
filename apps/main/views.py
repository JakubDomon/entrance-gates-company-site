from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from apps.main.models import mainContactForm
import json

# Create your views here.
def home(request):
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
            response = {'message': 'Nie zapisano wiadomości! Niepoprawne dane'}
            return JsonResponse(response, safe=False)

        # Check if input data is incorrect
        if((len(name) < 3) or ('@' not in email) or (len(text) < 10)):
            response = {'message': 'Nie zapisano wiadomości! Niepoprawne dane'}
            return JsonResponse(response, safe=False)

        # If data is correct - save to database
        record = mainContactForm(name=name, email=email, text=text, verificated = False, texted_back = False)
        record.save()

        response = {'message': 'Zapisano wiadomość'}
        return JsonResponse(response, safe=False)

    return redirect('/')