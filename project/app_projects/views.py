from xml.etree.ElementInclude import include
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.settings import PROJECT_MEDIA_ROOT, PROJECT_MEDIA_URL
from .forms import (
    CreateProjectForm,
    EditProjectForm
)
import os
from .models import ProjectModel



def view_post_project(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_validated:
            if request.POST:
                form = CreateProjectForm(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    form.author = user
                    form.save()
                    return redirect('dashboard')
            else:
                form = CreateProjectForm()
                context['form'] = form




            context['user'] = user
            return render(request, 'create-project.html', context)
        else:
            return redirect('dashboard')
    else:
        return redirect('login')



def view_edit_project(request):
    pass

'''
def view_edit_project(request):
    context = {}
    user = request.user
    #model = form.instance
    if user.is_authenticated:
        if user.is_validated:
            if request.POST:
                form = EditProjectForm(request.POST, request.FILES, instance=user)
                if form.is_valid():

                    form.save()
                    return redirect('dashboard')
            else:
                form = EditProjectForm(initial={
                    "title": title,
                    "description": title,
                    "type": title,
                    "building_area": title,
                    "cubic_capacity": title,
                    "height": title})




        else:
            return redirect('dashboard')
    else:
        return redirect('login')
'''


def template(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        context['user'] = user
        return render(request, 'activate.html', context)

    else:
        return redirect('login')



