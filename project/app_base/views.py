from django.shortcuts import (render, redirect)


def view_home(request):
    return render(request, 'home.html')

def view_about(request):
    return render(request, 'about.html')


def handler404(request):
    response = render("404.html")
    response.status_code = 404
    return response

def handler500(request):
    response = render("500.html")
    response.status_code = 500
    return response
