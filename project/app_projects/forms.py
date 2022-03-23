from dataclasses import fields
from django import forms
from . import models


class CreateProjectForm(forms.ModelForm):
    
    class Meta:
        model = models.ProjectModel
        fields = ('title', 'description', 'type', 'building_area', 'cubic_capacity', 'height')

class EditProjectForm(forms.ModelForm):
    
    class Meta:
        model = models.ProjectModel
        fields = ('title', 'description', 'type', 'building_area', 'cubic_capacity', 'height')





'''


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = models.ProjectModel
        fields = ('', '', )
class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = models.ProjectModel
        fields = ('', '', )

    '''