from django.db import models
from django.utils import timezone

# Create your models here.


class TodoListModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)

    def __unicode__(self):
        return("{}", format(self.title))
