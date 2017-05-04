import datetime
from django import forms
from hw6.models import *
from django.db import models


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','estimate','state']

def clean(self):
              try:
                _estimate = datetime.datetime.strptime(Task.estimate, "%Y-%m-%d")
              except:
                   forms.ValidationError('Please submit correct estimate format XXXX-XX-XX')

              if (Task.state != "ready") and (Task.state != "in_progress"):
                  forms.ValidationError('Please chose one of two states: in_progress or ready.')

              return self.cleaned_data

class RoadmapForm(forms.ModelForm):
    class Meta:
        model = Roadmap
        fields = ['roadmap_name']
