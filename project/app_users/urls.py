'''
path('urlname', views.function_name, name='path_name'),

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL_USER, document_root=settings.MEDIA_ROOT_USER)

'''

from django.urls import path
from . import views
import os
from main import settings
from django.conf.urls.static import static

urlpatterns = [
    path('account/register', views.view_register, name='register'),
    path('account/login', views.view_login, name='login'),
    path('account/logout', views.view_logout, name='logout'),
    path('dashboard', views.view_dashboard, name='dashboard'),



]