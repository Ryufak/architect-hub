from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from main.settings import PROJECT_MEDIA_ROOT
from .forms import (
    CreateProjectForm,
    EditProjectForm,
)
import os
from django.core.files.storage import FileSystemStorage
from .models import ProjectModel


def view_post_project(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_validated:
            if request.POST:
                form = CreateProjectForm(request.POST, request.FILES)
                if form.is_valid():
                    form_instance = form.save(commit=False)
                    form_instance.author = user
                    
                    path = os.path.join(PROJECT_MEDIA_ROOT, user.username, form_instance.ref_number)
                    fss = FileSystemStorage(location=path)
                    images = request.FILES.getlist('files')
                    i = 0
                    for image in images:
                        i += 1
                        file_name = f'image{i}.png'
                        if fss.exists(file_name):
                            fss.delete(file_name)
                        fss.save(file_name, image)

                    form_instance.save()
                    return redirect('dashboard')
                else:
                    context['form'] = form
            else:
                form = CreateProjectForm()
                context['form'] = form

            context['user'] = user
            return render(request, 'create-project.html', context)
        else:
            return redirect('dashboard')
    else:
        return redirect('login')

def view_edit_project(request, id):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_validated:
            try:
                project = ProjectModel.objects.filter(ref_number=id, author=user)[0]
                context['ref_number'] = project.ref_number
            except IndexError:
                raise Http404

            if request.POST:
                form = EditProjectForm(request.POST, request.FILES, instance=project)
                if form.is_valid():
                    form_instance = form.save(commit=False)
                    form_instance.author = user
                    
                    path = os.path.join(PROJECT_MEDIA_ROOT, user.username, form_instance.ref_number)
                    fss = FileSystemStorage(location=path)
                    images = request.FILES.getlist('files')
                    i = 0
                    for image in images:
                        i += 1
                        file_name = f'image{i}.png'
                        if fss.exists(file_name):
                            fss.delete(file_name)
                        fss.save(file_name, image)

                    form_instance.save()
                    return redirect('dashboard')
                else:
                    context['form'] = form
            else:
                form = EditProjectForm(initial={
                    "title": project.title,
                    "description": project.description,
                    "type": project.type,
                    "building_area": project.building_area,
                    "cubic_capacity": project.cubic_capacity,
                    "height": project.height,
                    "image_thumbnail": project.image_thumbnail})
                context['form'] = form  
            context['user'] = user
            return render(request, 'update-project.html', context)
        else:
            return redirect('dashboard')
    else:
        return redirect('login')

def view_delete_project(request, id):
    user = request.user
    if user.is_authenticated:
        if user.is_validated:
            try:
                project = ProjectModel.objects.filter(ref_number=id, author=user)[0]
            except IndexError:
                raise Http404

            path = os.path.join(PROJECT_MEDIA_ROOT, user.username)
            fss = FileSystemStorage(location=os.path.join(path, id))
            fss.delete('Thumbnail.png')
            i = 0
            while True:
                i += 1
                filename = f'image{i}.png'
                if fss.exists(filename):
                    fss.delete(filename)
                else:
                    break
            fss = FileSystemStorage(location=path)
            fss.delete(id)

            project.delete()

            return render(request, 'about.html')

        else:
            return redirect('dashboard')
    else:
        return redirect('login')



#_________________________________________________________
# Incomplete




def template(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        context['user'] = user
        return render(request, 'activate.html', context)

    else:
        return redirect('login')



