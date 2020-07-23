from django.http import HttpResponse
from django.shortcuts import redirect

#para que no pueda acceder sin logearse
def no_login_user(view_func):
    def wrapper_func(request, *arg,**kwags):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *arg, **kwags)

    return wrapper_func


#permisos de usuarios 
def permiso_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *arg,**kwags):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *arg,**kwags)
            else:
                return HttpResponse('Usuario no autorizado...')
        return wrapper_func
    return decorator

#solo para adminiatradore
def admin_only(view_func):
    def wrapper_func(request, *arg,**kwags):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'farmaceutico':
            return redirect('home')
        if group == 'administracion':

            return view_func(request, *arg,**kwags)

    return wrapper_func
