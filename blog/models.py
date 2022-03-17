from django.db import models
from django.forms import DateField


class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
