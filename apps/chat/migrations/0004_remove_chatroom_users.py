# Generated by Django 4.1.5 on 2023-03-21 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_chatroom_description_chatroom_creationdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='users',
        ),
    ]