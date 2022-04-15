
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from Database.models import Student,Professor
from django.db import IntegrityError
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', {'c': c})

    # messages.warning(request,"Invalid Username or Password")


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/login/loggedin/')
    else:
        return HttpResponseRedirect('/login/invalidlogin/')


def signup(request):
    try:
        username = request.POST.get('username', '')
        password = request.POST.get('password1', '')
        email = request.POST.get('email', '')
        user = User.objects.create_user(username, email, password)
        if(request.POST.get('professor',False)):
            profile = Professor.objects.create(user=user)
        else:
            profile = Student.objects.create(user=user)
        return HttpResponseRedirect('/login/')
    except IntegrityError :
        return render(request, 'invalidlogin.html', {'some_flag':True})
   

def loggedin(request):
    return HttpResponseRedirect('/database/home')


def invalidlogin(request):
    return render(request, 'invalidlogin.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')



# Create your views here.