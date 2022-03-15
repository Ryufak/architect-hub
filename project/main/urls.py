from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),

    # Including APPS' URLconfigs
    path('', include('app_base.urls')),
    path('', include('app_users.urls')),

]
