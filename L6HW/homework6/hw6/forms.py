import datetime
from django import forms
from hw6.models import *
from django.db import models


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'estimate', 'state']


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'estimate']

class RoadmapForm(forms.ModelForm):
    class Meta:
        model = Roadmap
        fields = ['roadmap_name']
