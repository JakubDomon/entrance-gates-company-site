from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length= 512)
    creationDate = models.DateTimeField(default=timezone.now)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # seen = models.BooleanField(default=False)

    # FK constraints
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, default=None)

    def messages_today(self) -> int:
        messages = self.filter('')

# class MessageStatistics(models.Model):
#     date = models.DateTimeField(default=timezone.now)