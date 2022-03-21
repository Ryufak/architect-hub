from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from . import models

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required')

    class Meta:
        model = models.CustomUser

        #Shows which fields pop up in the form
        fields = ("email", "username", "password1", "password2")

class CustomLoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = models.CustomUser
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Incorrect username or password.")

class UserActivateForm(forms.ModelForm):

    class Meta:
        model = models.CustomUser
        fields = ('activation_key',)

class CustomUserCredentialsForm(forms.ModelForm):

    class Meta:
        model = models.CustomUser
        fields = ('email', 'username')


    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = models.CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
            except models.CustomUser.DoesNotExist:
                return email
            raise forms.ValidationError('%s is already in use.' % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = models.CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
            except models.CustomUser.DoesNotExist:
                return username
            raise forms.ValidationError('The username %s is already in use.' % username)

class CustomUserValidationForm(forms.ModelForm):

    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name', 'country', 'city', 'certification')        

class CustomUserInfoForm(forms.ModelForm):

    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name', 'about', 'country', 'city', 'image_cover', 'image_profile')
        



