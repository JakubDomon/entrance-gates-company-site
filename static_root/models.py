from django.db import models

class mainContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    text = models.TextField()
    verificated = models.BooleanField(default=False)
    texted_back = models.BooleanField(default=False)

