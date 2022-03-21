# Generated by Django 4.0.3 on 2022-03-19 16:47

import app_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_customuser_image_cover_customuser_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image_cover',
            field=models.ImageField(blank=True, default='static/default_cover_picture.jpg', max_length=255, null=True, upload_to=app_users.models.CustomUser.profile_picture),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image_profile',
            field=models.ImageField(blank=True, default='static/default_profile_picture.jpg', max_length=255, null=True, upload_to=app_users.models.CustomUser.cover_photo),
        ),
    ]
