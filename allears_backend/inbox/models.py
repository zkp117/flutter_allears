from django.db import models
from django.db.models import ForeignKey
from allears_backend.users.models import User
class SelfInbox(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='self_inboxes')
    question = models.TextField()
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SelfInbox for {self.user.username} at {self.created_at}"
    class Meta:
        verbose_name = "Your Inbox"
        ordering = ['-received_at', 'questions', 'messages']

