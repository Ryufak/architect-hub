from django.shortcuts import (render, redirect)


def view_home(request):
    return render(request, 'home.html')

def view_about(request):
    return render(request, 'about.html')



