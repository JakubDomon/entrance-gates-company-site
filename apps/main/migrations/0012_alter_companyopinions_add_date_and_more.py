# Generated by Django 4.1.5 on 2023-03-09 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_companyopinions_add_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyopinions',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 14, 20, 44, 631211, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 14, 20, 44, 629812, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='maincontactform',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 14, 20, 44, 629411, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='opinions',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 14, 20, 44, 630887, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 14, 20, 44, 630512, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 14, 20, 44, 630101, tzinfo=datetime.timezone.utc)),
        ),
    ]