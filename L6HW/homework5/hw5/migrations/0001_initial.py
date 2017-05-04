# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roadmap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roadmap_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('estimate', models.DateField(error_messages={'required': 'Please submit correct estimate format XXXX-XX-XX'})),
                ('state', models.CharField(default='in_progress', error_messages={'required': 'Please chose one of two states: in_progress or ready.'}, max_length=100)),
                ('roadmap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw5.Roadmap')),
            ],
        ),
    ]