from django.contrib.auth.models import User
from functools import wraps
from django.core.exceptions import PermissionDenied

# Wrapper to restrict access to views based on user groups
def group_access(group: str):
    def wrap1(function):
        def func(request, *args, **kwargs):
            # Get current user
            user = request.user
            # Check if user group matches argument
            if user.groups.filter(name= group).exists():
                return function(request, *args, **kwargs)
            else:
                # If user group doesn't match argument, raise permission denied
                raise PermissionDenied()
        return func
    return wrap1