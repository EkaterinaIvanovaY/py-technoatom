# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('estimate', models.DateField(error_messages={'required': 'Please submit correct estimate format XXXX-XX-XX'})),
                ('state', models.CharField(default='in_progress', error_messages={'required': 'Please chose one of two states: in_progress or ready.'}, max_length=100)),
            ],
        ),
    ]
