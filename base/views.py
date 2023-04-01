from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate
from .models import *

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        UD = todo_list.objects.filter(User=request.user)
        return render(request, 'home.html', locals())
    else:
        return render(request, 'home.html')


def signin(request):
    if request.user.is_authenticated:
        UD = todo_list.objects.filter(User=request.user)
        # return render(request, 'home.html', locals())
        return redirect('/')
    else:    
        bug = ''
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['pwd']
            try:
                user = authenticate(request, username=username, password=password)
                if user.is_active:
                    # pass
                    login(request, user)
                    bug = 'no'
            except:
                bug = 'yes'
    return render(request, 'authenticate/signin.html', locals())



def signup(request):
    if request.user.is_authenticated:
        UD = todo_list.objects.filter(User=request.user)
        return redirect('/')
    else:
        bug = ''
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            pwd = request.POST['pwd']
            confirm_pwd = request.POST['confirm_pwd']

            if User.objects.filter(username=username).exists():
                bug = 'username_exists'
            elif User.objects.filter(email=email).exists():
                bug = 'email_exists'
            elif pwd != confirm_pwd:
                bug = 'pwd_miss_match'
            else:
                try:   
                    User.objects.create_user(username=username, email=email, password=pwd)
                    bug = 'no'
                except :
                    bug = 'yes'
        return render(request, 'authenticate/signup.html', locals())
    


def list_add(request):
    if request.user.is_authenticated:
        UD = todo_list.objects.filter(User=request.user)
        if request.method == 'POST':
            title = request.POST['title']
            desc = request.POST['descr']
            try:
                tdl = todo_list.objects.create(User=request.user, title=title, desc=desc)
                tdl.save()
                bug = 'list_added'
            except:
                bug = 'yes'
        return redirect('/')
    else:
        return redirect('/')

def list_view(request, pid):
    vtls = todo_list.objects.get(id=pid)
    return render(request, 'list_view.html', locals())

def list_update(request, pid):
    if request.user.is_authenticated:
        bug = ''
        etdi = todo_list.objects.get(id=pid)
        try:

            if request.method == 'POST':
                title = request.POST['title']
                desc = request.POST['desc']
                etdi.title = title
                etdi.desc = desc
                etdi.save()
                bug = 'updated'
        except:
            bug = 'not_updated'
        return render(request, 'list_update.html', locals())
    else:
        return render(request, 'home.html')
        

def list_app(request, pid):
    vtls = todo_list.objects.get(id=pid)
    vtls.is_complete = True
    vtls.save()
    return redirect('/')

def list_rej(request, pid):
    vtls = todo_list.objects.get(id=pid)        
    vtls.is_complete = False
    vtls.save()
    return redirect('/')

    
def list_delete(request, pid):
    dtl = todo_list.objects.get(id=pid)
    dtl.delete()
    return redirect('/')


def Logout(request):
    logout(request)
    return redirect('/')