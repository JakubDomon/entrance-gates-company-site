from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from django.utils.decorators import method_decorator
from apps.authorize.forms import LoginForm, RegisterForm
from django.views.generic import View
from django.contrib.auth.models import User, Group, Permission
from django.contrib import messages
from cerberus import Validator
import json
# Create your views here.

def login_user(request):
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
                messages.success(request, 'Pomyślnie zalogowano użytkownika ' + user.get_username())
                return render(request, 'main/static/home.html', {'loginForm': loginForm})

            return render(request, 'main/static/home.html', {'loginForm': loginForm})
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

            messages.success(request, 'Pomyślnie dodano użytkownika!')

            return render(request, 'authorize/static/register.html', {'registerForm': registerForm, 'action': 'redirect'})
        else:
            messages.error(request, 'Nie udało się dodać użytkownika!')
            return render(request, 'authorize/static/register.html', {'registerForm': registerForm, 'action': 'redirect'})
    else:
        registerForm = RegisterForm()
        return render(request, 'authorize/static/register.html', {'registerForm': registerForm, 'action': 'none'})


@login_required
def logout_user(request):
    user = request.user.username
    logout(request)

    messages.success(request, 'Pomyślnie wylogowano użytkownika ' + user)
    
    loginForm = LoginForm()
    return render(request, 'main/static/home.html', {'loginForm': loginForm})


# Permission management
# Base GroupView class
@method_decorator(login_required, name='dispatch')
class GroupView(View):

    def get(self, request):
        returnList = {}
        for group in Group.objects.all():
            userSet = list(group.user_set.all().values('username'))
            permissionSet = list(group.permissions.all().values('name', 'codename'))


            var = {
                'name': group.name,
                'users': userSet,
                'permissions': permissionSet,
            }
            returnList[group.name] = var

        return JsonResponse({'Groups': returnList})

# Class to manage Groups
# Actions:
# - add_group
# - delete_group
# - add_user_to_group
# - delete_user_from_group
class ManageGroups(GroupView):
    
    def post(self, request):
        # Get data from post request
        data = json.loads(request.body.decode('utf-8'))
        
        # Get type of action
        # Not sweet solution of switch-case - Python 3.10 greets :(
        try:
            if data['action'] == 'add_group':
                # Validation schema
                schema = {
                    'group-name': {'type': 'string', 'minlength': 3, 'maxlength': 15},
                    'permissions': {'type': 'list', 'schema':{'type': 'string'}},
                    'users': {'type': 'list', 'schema': {'type': 'integer'}},
                    'action': {'type': 'string'},
                    }
                
                # Validator instance
                v = Validator(schema)

                # Validate input
                if v.validate(data):
                    # Assign values to variables
                    try:
                        # Permission - dict as key(alias)->value(string permission word)
                        groupName = data['group-name']
                        permissions = data['permissions']
                        users = data['users']
                    except:
                        response = {
                            'message': 'Dane nieprawidłowe!',
                        }
                        return JsonResponse(response)
                    
                    # Add new group
                    if not Group.objects.filter(name=groupName):
                        newGroup, created = Group.objects.get_or_create(name=groupName)
                        # Asign permissions to group
                        for perm in permissions:
                            p = Permission.objects.get(codename=perm)
                            newGroup.permissions.add(p)

                        # Asign users to group
                        userArr = []
                        for user in users:
                            if User.objects.filter(id=user).exists():
                                userArr.append(User.objects.filter(id=user).get())

                        # Add user to group
                        if userArr:
                            for user in userArr:
                                user.groups.add(newGroup)

                        # Send success response
                        response = {
                                'message': 'Dodano grupę!',
                            }
                        return JsonResponse(response)
                    
                    # Send error response
                    response = {
                            'message': 'Podana nazwa grupy już istnieje!',
                        }
                    return JsonResponse(response)
                else:
                    return JsonResponse({'message': 'Błąd!'})
            elif data['action'] == 'delete_group':
                pass

            elif data['action'] == 'add_user_to_group':
                pass

            elif data['action'] == 'delete_user_from_group':
                pass
        except:
            response = {
                'message': 'Dane nieprawidłowe!',
            }
            return JsonResponse(response)