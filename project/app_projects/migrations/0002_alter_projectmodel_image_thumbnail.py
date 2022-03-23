# Generated by Django 4.0.3 on 2022-03-23 19:53

import app_projects.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='image_thumbnail',
            field=models.ImageField(max_length=255, null=True, upload_to=app_projects.models.ProjectModel.thumbnail_image, verbose_name='Thumbnail image'),
        ),
    ]
