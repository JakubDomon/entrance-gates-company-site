from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length= 512)
    description = models.CharField(max_length= 1024)


class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    # FK constraints
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, default=None)