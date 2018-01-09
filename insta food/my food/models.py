from django.db import models
from django.utils import timezone

class lampung(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return (self.title + '<br>' + self.body + '\n')

class jakarta(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return (self.title + '<br>' + self.body + '\n')

class bali(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return (self.title + '<br>' + self.body + '\n')
