from django.urls import path
from . import views

urlpatterns = [

    path('project/post', views.view_post_project, name='project-post'),
    path('project/edit', views.view_edit_project, name='project-edit'),


]