# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-31 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]