from django.db import models
from main.utilities import simple_uuid
import os
from app_users.models import CustomUser


class ProjectModel(models.Model):
    
    ref_number          = models.CharField(default=simple_uuid, max_length=36, editable=False)
    author              = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    created             = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated        = models.DateTimeField(verbose_name='Last updated', auto_now=True, editable=False)

    TYPES = (('residential', 'Residential'), ('commercial', 'Commercial'), ('industrial', 'Industrial'),)

    title               = models.CharField(max_length=30, blank=True)
    description         = models.CharField(max_length=600, blank=True)
    type                = models.CharField(max_length=20, choices=TYPES, default=TYPES[0])
    building_area       = models.DecimalField(verbose_name='Building area', max_digits=5, decimal_places=2, default=0, blank=True)
    cubic_capacity      = models.DecimalField(verbose_name='Cubic capacity', max_digits=5, decimal_places=2, default=0, blank=True)
    height              = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)

    #images







