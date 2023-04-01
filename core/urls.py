"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static


from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name = 'home'),
    
    # Authentication ----------------------------------------------------------------
    path('signin/', signin, name = 'signin.html'),
    path('signup/', signup, name = 'signup.html'),
    path('Logout/', Logout, name = 'Logout'),


    # List operations ----------------------------------------------------------------
    path('list_add', list_add, name = 'list_add'),
    path('list_view/<int:pid>', list_view, name='list_view'),
    path('list_update/<int:pid>', list_update, name='list_update'),
    path('list_delete/<int:pid>', list_delete, name='list_delete'),


    # list status --------------------------------------------------------------------
    path('list_app/<int:pid>/', list_app , name="list_app" ),
    path('list_rej/<int:pid>/', list_rej , name="list_rej" ),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)