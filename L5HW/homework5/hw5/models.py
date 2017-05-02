import datetime
from django.db import models
from django.core.urlresolvers import reverse


class Task(models.Model):
    title = models.CharField(max_length=100)
    estimate = models.DateField(error_messages=
                                {'required': 'Please submit correct estimate format XXXX-XX-XX'})
    state = models.CharField(default='in_progress', max_length=100,
                             error_messages=
                             {'required': 'Please choose one of two states: in_progress or ready.'})

    iscritical = property()

    @iscritical.getter
    def iscritical(self):
        date = datetime.date.today()
        delta = self.estimate - date
        days = datetime.timedelta(days=delta.days)
        if ( days < datetime.timedelta( days=3 ) ) and ( self.state == 'in_progress' ):
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('task_edit', kwargs={'pk': self.pk})
