from functools import wraps

from django.http import JsonResponse


def is_admin(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):

        type = request.user.is_admin
        if type:
            return function(request, *args, **kwargs)
        else:
            return JsonResponse({'message': 'You must be admin to proceed'})

    return wrap


