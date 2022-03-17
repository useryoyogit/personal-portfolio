from pyexpat import model
from turtle import title
from unicodedata import name
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class SocialAcc(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    header = models.CharField(max_length=40)
    title = models.CharField(blank=True, max_length=100)
    text = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.header
