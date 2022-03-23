from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from main.settings import USER_MEDIA_ROOT, STATIC_MEDIA_ROOT, admin_email
from .forms import (
    CustomRegistrationForm,
    CustomLoginForm,
    CustomUserCredentialsForm,
    UserActivateForm,
    CustomUserValidationForm,
    CustomUserInfoForm
    )
import os
from main.mail_templates import mail_activation_key, validation_email_ping
from django.core.files.storage import FileSystemStorage




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

def view_register(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        if request.POST:
            form = CustomRegistrationForm(request.POST)

            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(email=email, password=raw_password)
                login(request, user)

                # Sends activation key to email
                email = user.email
                username = user.username
                activation_key = user.activation_key
                mail_activation_key(username, email, activation_key)
                
                return redirect('activate')
            else:
                context['registration_form'] = form
        else:
            form = CustomRegistrationForm()
            context['registration_form'] = form
        return render(request, 'register.html', context)
    else:
        return redirect('dashboard')


def view_activate(request):
    context = {}
    context['admin_email'] = admin_email
    user = request.user
    if user.is_authenticated:
        if user.is_activated:
                return redirect('dashboard')
        else:
            if request.POST:
                form = UserActivateForm(request.POST, instance=user)
                real_key = user.activation_key
                key = request.POST['activation_key']
                if real_key == key:
                    user.is_activated = True
                    form.save()
                    return redirect('dashboard')
                else:
                    context['val_error'] = 'The key you entered is Invalid.'
            else:
                form = UserActivateForm(instance=user, initial={'activation_key': ''})  
            context['form'] = form
            context['user'] = user
            return render(request, 'activate.html', context)
    else:
        return redirect('login')

def resend_key(request): # Needs CAPTCHA against request spamming
    user = request.user
    if user.is_authenticated:
        if user.is_activated:
            redirect('dashboard')
        else:
            # Re-Sends activation key to email
            email = user.email
            username = user.username
            activation_key = user.activation_key
            mail_activation_key(username, email, activation_key)

            return HttpResponse('<script>window.close()</script>')
    else:
        return redirect('login')


def view_change_credentials(request):   # Also changes user folder name
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_activated:
            if request.POST:
                form = CustomUserCredentialsForm(request.POST, instance=user)
                old_username = os.path.join(USER_MEDIA_ROOT, str(user.username))
                if form.is_valid():
                    new_username = os.path.join(USER_MEDIA_ROOT, str(form.cleaned_data.get('username')))
                    os.rename(old_username, new_username)
                    form.save()
                    context['message'] = 'Details changed successfully'
            else:
                form = CustomUserCredentialsForm(initial={
                    "email": user.email,
                    "username": user.username,})
            context['credentials_form'] = form
            return render(request, "credentials.html", context)
        else:
            return redirect('activate')
    else:
        return redirect('login')

def view_validation(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_validated or user.pending_validation:
            return redirect('dashboard')
        else:
            if request.POST:
                form = CustomUserValidationForm(request.POST, request.FILES['id_image'], instance=user)
                if form.is_valid():
                    user.pending_validation = True
                    form.save()

                    path = os.path.join(STATIC_MEDIA_ROOT, 'temp', user.activation_key)
                    fss = FileSystemStorage(location=path)
                    upload = request.FILES['id_image']
                    file = fss.save('image.png', upload)
                    attachment = f'{path}/image.png'
                    
                    try:
                        validation_email_ping(user.username, user.email, attachment)
                    except BadHeaderError:
                        fss.delete('image.png')
                        return HttpResponse('Invalid header!')
                    fss.delete('image.png')
                    
                    return redirect('dashboard')
            else:
                form = CustomUserValidationForm()
                context['form'] = form
            context['user'] = user
            return render(request, 'validate.html', context)
    else:
        return redirect('login')

def view_update(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if request.POST:
            form = CustomUserInfoForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = CustomUserInfoForm(initial={
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "country": user.country,
                    "city": user.city,
                    "about": user.about,})
            context['form'] = form
        context['user'] = user
        return render(request, 'user-update.html', context)
    else:
        return redirect('login')

def view_delete(request):
    user = request.user
    if user.is_authenticated:
        user.delete()
        logout(request)
        return redirect('home')
    else:
        return redirect('login')



#_________________________________________________________
# Incomplete
def view_dashboard(request):
    user = request.user
    context = {'user': user,}
    if user.is_authenticated:
        if not user.is_activated:
                return redirect('activate')
        else:
            return render(request, 'dashboard.html', context)
        #add context
    else:
        return redirect('login')


















def template(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        context['user'] = user
        return render(request, 'activate.html', context)

    else:
        return redirect('login')








