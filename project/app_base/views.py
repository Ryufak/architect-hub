from django.shortcuts import (render, redirect)
import os



def view_home(request):
    return render(request, 'home.html')

def view_about(request):
    return render(request, 'about.html')

def view_architects(request):
    #build
    pass

def view_upload_project(request):
    pass
    #build