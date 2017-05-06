import datetime
from django import forms
from hw6.models import *
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'estimate', 'state']
        widgets = {
            'estimate': SelectDateWidget(years=range(1960, 2100)),
        }

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'estimate']
        widgets = {
            'estimate': SelectDateWidget(years=range(1960, 2100)),
        }
class RoadmapForm(forms.ModelForm):
    class Meta:
        model = Roadmap
        fields = ['roadmap_name']
