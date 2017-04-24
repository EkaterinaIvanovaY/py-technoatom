from django.db import models
import datetime


class Task(models.Model):
    _title = models.CharField(max_length=30)
    _estimate = models.DateField()



