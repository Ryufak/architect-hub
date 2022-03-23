from django.db import models
from main.utilities import simple_uuid
import os
from main.settings import AUTH_USER_MODEL, PROJECT_MEDIA_ROOT


class ProjectModel(models.Model):
    
    ref_number          = models.CharField(default=simple_uuid, max_length=36, editable=False)
    author              = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True, unique=False, db_constraint=False)
    created             = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated        = models.DateTimeField(verbose_name='Last updated', auto_now=True, editable=False)

    TYPES = (('residential', 'Residential'), ('commercial', 'Commercial'), ('industrial', 'Industrial'),)

    title               = models.CharField(max_length=30, blank=True)
    description         = models.CharField(max_length=600, blank=True)
    type                = models.CharField(max_length=20, choices=TYPES, default=TYPES[0])
    building_area       = models.DecimalField(verbose_name='Building area', max_digits=5, decimal_places=2, default=0, blank=True)
    cubic_capacity      = models.DecimalField(verbose_name='Cubic capacity', max_digits=5, decimal_places=2, default=0, blank=True)
    height              = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)

    def thumbnail_image(instance, filename):
        upload_to = os.path.join(PROJECT_MEDIA_ROOT, str(instance.author.username), str(instance.ref_number))
        file = str(upload_to + '/Thumbnail.png')
        if os.path.exists(file) is True: os.remove(file)
        return file
    image_thumbnail     = models.ImageField(upload_to=thumbnail_image, max_length=255, null=True, blank=False, verbose_name='Thumbnail image')


    def __str__(self):
        return self.title


