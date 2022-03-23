from django import forms
from . import models


class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = models.ProjectModel
        fields = ('title', 'description', 'type', 'building_area', 'cubic_capacity', 'height', 'image_thumbnail')
     
class EditProjectForm(forms.ModelForm):
    
    class Meta:
        model = models.ProjectModel
        fields = ('title', 'description', 'type', 'building_area', 'cubic_capacity', 'height', 'image_thumbnail')


