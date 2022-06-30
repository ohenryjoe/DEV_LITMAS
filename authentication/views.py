# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        us = request.POST.get('username')
        pw = request.POST.get('password')
        if form.is_valid():
            username = us
            password = pw
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_staff:
                    return redirect("/")
                else:
                    return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "authentication/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "authentication/register.html", {"form": form, "msg": msg, "success": success})


def auth_register(request):
    return render(request, 'authentication/register.html')


def auth_lockscreen(request):
    logout(request)
    return render(request, 'authentication/lockscreen.html')


def auth_logout(request):
    logout(request)
    return redirect('auth_login')


def auth_password_change(request):
    return None


def auth_password_change_done(request):
    return None


def auth_password_reset(request):
    return None


def auth_password_reset_done(request):
    return None


def reset(request):
    return None


def reset_complete(request):
    return None