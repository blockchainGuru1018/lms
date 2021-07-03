from functools import wraps
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required


def teacher_required_dec(func):

    @wraps(func)
    def wrapper(request, *args, **kw):
        
        if request.user.is_teacher:
            return func(request, *args, **kw)
        return redirect(settings.LOGIN_URL)

    return wrapper


teacher_decorators = (login_required, teacher_required_dec,)
