from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib import messages

from .forms import CreateUserForm,EditUserForm
from .models import *

from .decorators import no_login_user,permiso_users,admin_only



@login_required(login_url='login')

#@permiso_users(allowed_roles=['farmaceutico'])
#@admin_only 
def layout(request):
    return render(request,'index.html')

def data(request):
    return render(request,'data.html')

@no_login_user
def registerPage(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='farmaceutico')
            user.groups.add(group)
            Setting.objects.create(
                user_id=user,
                )#relacion con la tabla de setting

            messages.success(request, 'Se creó una cuenta para ' + username + ' puede Ingresar..')
            return redirect('login')

    context = {'form': form}
    return render(request, 'registro.html', context)


@no_login_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is  not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'EL email o la contraseña no son correctos...')

    context = {}
    return render(request, 'login.html', context)

def loginOut(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def userSetting(request):
    setting = request.user.setting
    form = EditUserForm(instance=setting)

    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=setting)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'setting.html', context)

# link-dark - este partado es para el cambio de fondoss


