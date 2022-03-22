from django.urls import path
from . import views

urlpatterns = [
    path('account/register', views.view_register, name='register'),
    path('account/login', views.view_login, name='login'),
    path('account/logout', views.view_logout, name='logout'),
    path('account/activate', views.view_activate, name='activate'),
    path('account/activate/resend', views.resend_key, name='resend_key'),
    path('dashboard', views.view_dashboard, name='dashboard'),
    path('account/credentials', views.view_change_credentials, name='credentials'),
    path('account/validation', views.view_validation, name='validation'),
    path('account/update', views.view_update, name='update-profile'),
    path('account/delete', views.view_delete, name='delete-account'),
    
    
    
    
    path('project/post', views.view_post_project, name='post'),
    #architects

    







]