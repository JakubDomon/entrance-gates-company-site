from django.contrib import admin
from .models import MainCategory, Product, Opinions
# Register your models here.

admin.site.register(MainCategory)
admin.site.register(Product)
admin.site.register(Opinions)