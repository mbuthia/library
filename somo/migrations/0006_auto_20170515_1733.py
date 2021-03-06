# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 17:33
from __future__ import unicode_literals

import Somo.settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('somo', '0005_remove_book_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myrequest',
            name='course',
        ),
        migrations.RemoveField(
            model_name='myrequest',
            name='user',
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='book',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[Somo.settings.validate_file]),
        ),
        migrations.DeleteModel(
            name='MyRequest',
        ),
    ]
