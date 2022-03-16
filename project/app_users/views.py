from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomRegistrationForm, CustomLoginForm
import os


def view_dashboard(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return render(request, 'dashboard.html', context)
        #add data
    else:
        return redirect('login')



def view_register(request):
    context = {}
    if request.POST:
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('dashboard')
        else:
            context['registration_form'] = form
    else:
        form = CustomRegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)

def view_login(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')

    if request.POST:
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomLoginForm()
    context['login_form'] = form
    return render(request, 'login.html', context)

def view_logout(request):
    logout(request)
    return redirect('home')