from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from apps.authorize.auth import group_access

# Create your views here.
@login_required
@group_access('Staff')
def admin_panel(request):
    user = request.user
    
    return render(request, 'admin_panel/static/admin_panel.html', {'user': user})