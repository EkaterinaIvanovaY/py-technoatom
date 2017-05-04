import datetime
from django.db import models
from django.core.urlresolvers import reverse


class Roadmap(models.Model):
    roadmap_name = models.CharField(max_length=100)

    today = property()
    @today.getter
    def today(self):
        today_tasks = []
        for task in self.tasks:
            if task.estimate == datetime.date.datetime:
                today_tasks.append(task.title)
        return today_tasks

    def filter(self, state):
        state_tasks = []
        for task in self.tasks:
            if state == task.state:
                state_tasks.append(task.title)
        return state_tasks

class Task(models.Model):
    title = models.CharField(max_length=30)
    estimate = models.DateField(error_messages={'required': 'Please submit correct estimate format XXXX-XX-XX'})
    state = models.CharField(default='in_progress',max_length=100,error_messages={'required': 'Please chose one of two states: in_progress or ready.'})
    roadmap = models.ForeignKey(Roadmap,on_delete=models.CASCADE)

    iscritical = property()
    @iscritical.getter
    def iscritical(self):
        date = datetime.date.today()
        delta = self.estimate - date
        days = datetime.timedelta(days=delta.days)
        if ( days < datetime.timedelta(days=3) ) and (self.state == 'in_progress'):
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('task_edit', kwargs={'pk': self.pk})


