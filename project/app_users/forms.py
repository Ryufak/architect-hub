from django import forms
from django.contrib.auth.forms import UserCreationForm

from project.app_users.admin import AccountAdmin
from . import models

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required')

    class Meta:
        model = models.CustomUser

        #Shows which fields pop up in the form
        fields = ("email", "username", "password1", "password2")