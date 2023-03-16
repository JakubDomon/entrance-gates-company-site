from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class MainCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    img = models.FileField(upload_to='media/products/categories')
    visible = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    add_date = models.DateTimeField(default=timezone.now)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    visible = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    img = models.FileField(upload_to='media/prodcuts/products/')
    add_date = models.DateTimeField(default=timezone.now)

    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

class Opinions(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    add_date = models.DateTimeField(default=timezone.now)
    accepted = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)