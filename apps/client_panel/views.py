from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def client_panel(request):
    user = request.user

    return render(request, 'client_panel/static/client_panel.html', {'user': user})