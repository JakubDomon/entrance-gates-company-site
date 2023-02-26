from django.db import models
from django.utils import timezone
import datetime

class MainContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    verificated = models.BooleanField(default=False)
    texted_back = models.BooleanField(default=False)

class MainCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    img = models.CharField(max_length=2056, default=None)
    visible = models.BooleanField(default=True)
    added_by = models.IntegerField()
    add_date = models.DateTimeField(default=timezone.now())

class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    img = models.CharField(max_length=2056, default=None)
    visible = models.BooleanField(default=True)
    added_by = models.IntegerField()
    add_date = models.DateTimeField(default=timezone.now())

    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    visible = models.BooleanField(default=True)
    img = models.CharField(max_length=2056, default=None)
    added_by = models.IntegerField()
    add_date = models.DateTimeField(default=timezone.now())

    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

class Opinions(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    add_date = models.DateTimeField(default=timezone.now())
    accepted = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class CompanyOpinions(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    add_date = models.DateTimeField(default=timezone.now())
    accepted = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)




