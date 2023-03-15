from django.db import models
from django.utils import timezone
import datetime

class MainContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    verificated = models.BooleanField(default=False)
    texted_back = models.BooleanField(default=False)

class CompanyOpinions(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    add_date = models.DateTimeField(default=timezone.now)
    accepted = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)




