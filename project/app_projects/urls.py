from django.urls import path
from . import views

urlpatterns = [

    path('project/post', views.view_post_project, name='project-post'),
    path('project/edit/<str:id>', views.view_edit_project, name='project-edit'),
    path('project/delete/<str:id>', views.view_delete_project, name='project-delete'),
    path('project/<str:id>', views.project_page, name='project-page'),

]