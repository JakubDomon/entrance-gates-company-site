from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.authorize.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method == 'POST':
        # Form instance
        loginForm = LoginForm(request.POST)

        # Check if form is valid
        if loginForm.is_valid():
            name = loginForm.cleaned_data['user_name']
            password = loginForm.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=name, password=password)

            # Login User
            if user is not None:
                login(request, user)
                redirect('/')

            redirect('/')
    else:
        loginForm = LoginForm()
    return render(request, 'main/static/home.html', {'loginForm': loginForm})

def register(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            name = registerForm.cleaned_data['user_name']
            email = registerForm.cleaned_data['email']
            password = registerForm.cleaned_data['password']

            user = User.objects.create_user(name, email, password)

            return render(request, 'auth/static/successCreateUser.html')
        else:
            attr = {
                'registerForm': registerForm,
                'message': 'Nieprawidłowe dane',
            }

            return render(request, 'auth/static/register.html', {attr})
    else:
        registerForm = RegisterForm()
        return render(request, 'authorize/static/register.html', {'registerForm': registerForm})
