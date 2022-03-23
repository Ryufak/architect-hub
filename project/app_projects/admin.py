from .models import ProjectModel
from django.contrib import admin



class ProjectsAdmin(admin.ModelAdmin):
    #Shows properties defined in the class in models.py
    list_display = ('author', 'title', 'created', 'last_updated')
    #Shows which fields can be searched
    search_fields = ('author', 'title')
    #Doesn't let you change those fields
    readonly_fields = ('ref_number', 'created', 'last_updated')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('author',)

admin.site.register(ProjectModel, ProjectsAdmin)




