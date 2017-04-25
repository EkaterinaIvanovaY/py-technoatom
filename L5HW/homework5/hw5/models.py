import datetime
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=30)
    estimate = models.DateField()
    state = models.CharField(default='in_progress',max_length=100)

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

