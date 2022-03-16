from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


from app_users.admin import AccountAdmin
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




