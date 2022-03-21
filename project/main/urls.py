from django.contrib import admin
from django.urls import path, include
from .settings import STATIC_URL, STATIC_MEDIA_ROOT, USER_MEDIA_URL, USER_MEDIA_ROOT
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app_base.urls')),
    path('', include('app_users.urls')),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(STATIC_URL, document_root=STATIC_MEDIA_ROOT)
urlpatterns += static(USER_MEDIA_URL, document_root=USER_MEDIA_ROOT)

