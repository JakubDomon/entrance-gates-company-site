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
from django.db.models import Q
from functools import reduce
from operator import or_
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
            # Query database
            userSet = list(group.user_set.all().values('username'))
            permissionSet = list(group.permissions.all().values('name', 'codename'))

            # Construct JSON
            var = {
                'id': group.id,
                'name': group.name,
                'users': userSet,
                'permissions': permissionSet,
            }
            returnList[group.name] = var
        
        # Return JSON data
        return JsonResponse({'Groups': returnList})

# Class to manage Groups
# Actions:
# - add_group --> just for tests
# - delete_group --> just for tests
# - add_users
# - delete_users
class ManageGroups(GroupView):
    
    def post(self, request):
        # Get data from post request
        data = json.loads(request.body.decode('utf-8'))
        
        # Validation schema
        schema = {
            'group-id': {'type': 'integer'},
            'users-id': {'type': 'list', 'minlength': 1, 'schema': {'type': 'integer'}},
            'action': {'type': 'string'},
        }

        # Validator instance
        v = Validator(schema)

        if v.validate(data):
            # Assign values to variables
            try:
                groupId = data['group-id']
                usersId = data['users-id']
                action = data['action']
            except:
                response = {
                    'message': 'Dane nieprawidłowe!',
                }
                return JsonResponse(response)
            
            # Search for group in database
            group = Group.objects.filter(id= groupId)
            # Search for users in database
            userConditions = reduce(or_, (Q(id=usrID) for usrID in usersId))
            
            # Query database
            users = User.objects.filter(userConditions)

            # Delete users from group
            try:
                if action == 'add_user_to_group':
                    for user in users:
                        user.groups.add(group)
                    
                    # Send success message
                    response = {
                        'message': 'Pomyślnie dodano użytkowników do grupy!',
                    }
                    return JsonResponse(response)
                
                elif action == 'delete_user_from_group':
                    for user in users:
                        user.groups.remove(group)
                    
                    # Send success message
                    response = {
                        'message': 'Pomyślnie usunięto użytkowników z grupy!',
                    }
                    return JsonResponse(response)
                
            except:
                response = {
                    'message': 'Wystąpił błąd!',
                }
                return JsonResponse(response)
            
        response = {
                'message': 'Niepoprawne dane!',
            }
        return JsonResponse(response)
    
        # <----------------- ONLY FOR TESTS ------------------------------>
        # Get type of action
        # Not sweet solution of switch-case - Python 3.10 greets :(
        # Adding and deleting groups are just for tests

        # # Add group, permissions and users
        # if data['action'] == 'add_group':
        #     # Validation schema
        #     schema = {
        #         'group-name': {'type': 'string', 'minlength': 3, 'maxlength': 15},
        #         'permissions': {'type': 'list', 'schema':{'type': 'string'}},
        #         'users': {'type': 'list', 'schema': {'type': 'integer'}},
        #         'action': {'type': 'string'},
        #         }
            
        #     # Validator instance
        #     v = Validator(schema)

        #     # Validate input
        #     if v.validate(data):
        #         # Assign values to variables
        #         try:
        #             # Permission - dict as key(alias)->value(string permission word)
        #             groupName = data['group-name']
        #             permissions = data['permissions']
        #             users = data['users']
        #         except:
        #             response = {
        #                 'message': 'Dane nieprawidłowe!',
        #             }
        #             return JsonResponse(response)
                
        #         # Add new group
        #         if not Group.objects.filter(name=groupName):
        #             newGroup, created = Group.objects.get_or_create(name=groupName)
        #             # Asign permissions to group
        #             for perm in permissions:
        #                 p = Permission.objects.get(codename=perm)
        #                 newGroup.permissions.add(p)

        #             # Asign users to group
        #             userArr = []
        #             for user in users:
        #                 if User.objects.filter(id=user).exists():
        #                     userArr.append(User.objects.filter(id=user).get())

        #             # Add user to group
        #             if userArr:
        #                 for user in userArr:
        #                     user.groups.add(newGroup)

        #             # Send success response
        #             response = {
        #                     'message': 'Dodano grupę!',
        #                 }
        #             return JsonResponse(response)
                
        #         # Send error response
        #         response = {
        #                 'message': 'Podana nazwa grupy już istnieje!',
        #             }
        #         return JsonResponse(response)
        #     else:
        #         return JsonResponse({'message': 'Błąd!'})

        # # Delete group
        # elif data['action'] == 'delete_group':
        #     # Validation schema
        #     schema = {
        #         'group-id': {'type': 'integer'},
        #         'action': {'type': 'string'},
        #     }

        #     # Validator instance
        #     v = Validator(schema)

        #     if v.validate(data):
        #         # Assign values to variables
        #         try:
        #             groupId = data['id']
        #         except:
        #             response = {
        #                 'message': 'Dane nieprawidłowe!',
        #             }
        #             return JsonResponse(response)
                
        #         # Search for group in database
        #         group = Group.objects.filter(id= groupId)
        #         # Delete group
        #         try:
        #             group.delete()
                    
        #             # Send success message
        #             response = {
        #                 'message': 'Usunięto grupę!',
        #             }
        #             return JsonResponse(response)
                
        #         except:
        #             response = {
        #                 'message': 'Wystąpił błąd podczas usuwania grupy!',
        #             }
        #             return JsonResponse(response)