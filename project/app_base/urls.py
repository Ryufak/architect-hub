from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_home, name='home'),
    path('about', views.view_about, name='about'),
    path('', views.handler404, name='404'),
    path('', views.handler500, name='500'),



]

