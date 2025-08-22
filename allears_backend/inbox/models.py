from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    anomymous = models.BooleanField(default=False)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.anomymous:
            return f'Anonymous message to {self.recipient.username} at {self.timestamp}'
        else:
            return f'Message from {self.sender.username} to {self.recipient.username} at {self.timestamp}'
    