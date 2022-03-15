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
    path('', views.view_home, name='home'),
    path('about', views.view_about, name='about'),
    path('architects', views.view_architects, name='architects'),
    path('upload', views.view_upload_project, name='upload_project'),
    



]

