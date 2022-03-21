from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class AccountAdmin(UserAdmin):
    #Shows properties defined in the CustomUser class in models.py
    list_display = ('email', 'username', 'pending_validation', 'is_activated', 'is_validated', 'is_admin', 'is_staff', 'is_superuser', 'date_joined', 'last_login', 'is_active')
    #Shows which fields can be searched
    search_fields = ('email', 'username')
    #Doesn't let you change those fields
    readonly_fields = ('date_joined', 'last_login', 'is_superuser')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomUser, AccountAdmin)