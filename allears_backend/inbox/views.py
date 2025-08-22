from .models import SelfInbox
from allears_backend.users.models import User, SelfInbox
from django.shortcuts import render

questions = SelfInbox.objects.filter(user=request.user, question__isnull=False)
messages = SelfInbox.objects.filter(user=request.user, message__isnull=False)

def inbox_view(request):
    if questions:
        questions = User.objects.filter(questions)
        
    elif messages:
        messages = User.objects.filter(messages)

    else:
        User.objects.filter(questions, messages)