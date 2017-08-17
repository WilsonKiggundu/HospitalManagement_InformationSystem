from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.conf import settings

from .forms import *


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/users/create/')
        elif not user.is_active:
            return render(request, 'login.html', {
                'message': 'Your account is inactive',
                'username': username
            })
        else:
            return render(request, 'login.html', {
                'message': 'Invalid username and/or password',
                'username': username
            })

    return render(request, "login.html", {
        'title': 'Login'
    })


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')


@login_required
def create_user(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, initial={'password': settings.DUMMY_PASSWORD})
        if user_form.is_valid():
            user = user_form.save()
            profile_form = ProfileForm(request.POST, instance=user)
            profile_form.save()
            return JsonResponse({
                'message': 'User added successfully',
                'type': 'success'
            })
        else:
            return JsonResponse({
                'message': 'Unable to add user',
                'type': 'error'
            })
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'form.html', {'form': [user_form, profile_form]})


def home(request):
    """Renders the home page"""
    return render(request, "index.html", {'title': 'Dashboard'})
