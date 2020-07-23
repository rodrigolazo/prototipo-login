"""SPDI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,login_required
from app.main import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('admin/',admin.site.urls),
    
    path('ini/', views.layout, name = 'home'),
    
    path('', views.loginPage, name = 'login'),
    path('registro', views.registerPage, name = 'register'),
    path('logout/', views.loginOut, name = 'logout'),

    path('data/', views.data, name = 'data'),
    
    #Configuracion

    path('configuracion/',views.userSetting, name = 'setting'),

    
]


urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)