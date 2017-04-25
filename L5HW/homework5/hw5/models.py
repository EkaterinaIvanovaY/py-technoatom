import datetime
from django.db import models

def date(_estimate):
    date = datetime.date.today()
    delta = _estimate - date
    days = datetime.timedelta(days = delta.days)
    return days
class Task(models.Model):
    title = models.CharField(max_length=30)
    estimate = models.DateField()
    state = models.CharField(max_length=10)
    days = models.DateField()

