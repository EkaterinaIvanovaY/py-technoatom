from django import forms
from hw5.models import Task


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'estimate', 'state']


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'estimate']
