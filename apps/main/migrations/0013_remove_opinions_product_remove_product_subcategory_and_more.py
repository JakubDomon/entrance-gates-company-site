# Generated by Django 4.1.5 on 2023-03-13 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_companyopinions_add_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opinions',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.AlterField(
            model_name='companyopinions',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 13, 11, 42, 26, 802507, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='maincontactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 13, 11, 42, 26, 802173, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='MainCategory',
        ),
        migrations.DeleteModel(
            name='Opinions',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
