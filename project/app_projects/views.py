from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.settings import PROJECT_MEDIA_ROOT, PROJECT_MEDIA_URL
#from .forms import 
import os







def template(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        context['user'] = user
        return render(request, 'activate.html', context)

    else:
        return redirect('login')



