from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from apps.products.models import MainCategory, Product, Opinions
from apps.main.models import CompanyOpinions, MainContactForm
from apps.authorize.forms import LoginForm
from django.views.generic import TemplateView, FormView
import json

# # HOME VIEW
# def home(request):
#     # Getting products
#     loginForm = LoginForm()
    
#     return render(request, 'main/static/home.html', {'loginForm': loginForm})

# HOME VIEW
class HomeView(FormView):
    model = Product
    form_class = LoginForm
    context_object_name = 'products'
    template_name = 'main/static/home.html'
    
    
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

# VIEW TO SAVE OPINION
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

# VIEW TO GET ALL OPINIONS
def opinionsGet(request):
    if request.method == 'GET':
        try:
            all_records = CompanyOpinions.objects.values()
            print(all_records)
        except Exception as Err:
            response = {
                'message': 'Nie udało się pobrać opinii z bazy danych',
                'status': 'error',
                'error': str(Err), 
            }
            return JsonResponse(response, safe= False)
        
        response = {
            'status': 'success',
            'data': list(all_records),
        }

        return JsonResponse(response, safe= False)