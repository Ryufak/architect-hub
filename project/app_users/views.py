from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
import os

#delete me
def placeholder_function(request):
    test = 0
    context = {
        'var_name': test
    }
    #In the .html file use  {{ var_name }}

    return render(request, 'home.html', context)
