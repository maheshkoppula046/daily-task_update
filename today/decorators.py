# today/decorators.py

from django.contrib.auth.decorators import login_required
from django.utils.decorators import wraps
from django.shortcuts import redirect

def custom_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('unauthorized_access')  # Redirect to custom unauthorized access page
    return _wrapped_view
