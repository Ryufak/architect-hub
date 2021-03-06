# Generated by Django 4.0.3 on 2022-03-23 15:01

import app_users.models
from django.db import migrations, models
import main.utilities


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('activation_key', models.CharField(default=main.utilities.simple_uuid, max_length=36)),
                ('is_activated', models.BooleanField(default=False)),
                ('pending_validation', models.BooleanField(default=False)),
                ('is_validated', models.BooleanField(default=False)),
                ('first_name', models.TextField(max_length=20, verbose_name='First name')),
                ('last_name', models.TextField(max_length=20, verbose_name='Last name')),
                ('country', models.CharField(choices=[('Bulgaria', 'Bulgaria'), ('USA', 'USA'), ('Russia', 'Russia'), ('Vatican', 'The Vatican')], default=('Bulgaria', 'Bulgaria'), max_length=20)),
                ('city', models.TextField(max_length=30)),
                ('about', models.CharField(max_length=600)),
                ('certification', models.URLField()),
                ('image_cover', models.ImageField(blank=True, default='static/media/default_cover_picture.jpg', max_length=255, null=True, upload_to=app_users.models.CustomUser.cover_photo, verbose_name='Cover image')),
                ('image_profile', models.ImageField(blank=True, default='static/media/default_profile_picture.jpg', max_length=255, null=True, upload_to=app_users.models.CustomUser.profile_picture, verbose_name='Profile picture')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
