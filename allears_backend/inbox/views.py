from .models import SelfInbox, BlockedWord
from django.http import JsonResponse

def self_inbox_view(request):
    self_inbox_filter = request.GET.get('filter')
    blocked_words = list(BlockedWord.objects.filter(user=request.user).values_list('word', flat=True))
    questions = SelfInbox.objects.filter(user=request.user, question__isnull=False)
    messages = SelfInbox.objects.filter(user=request.user, message__isnull=False)

    def censored_content(content):
        for word in blocked_words:
            if word.lower() in content.lower():
                return{
                    'content': '⚠️ This message or question contains a blocked word. View anyway?',
                    'blocked': True,
                }
        return {'content': content, 'blocked': False}
        
    if self_inbox_filter == 'questions':
        questions = questions.order_by('-created_at')
        data = [{
            'id': q.id, 'question': censored_content(q.question)} 
            for q in questions]
        return JsonResponse({'questions': data})
    
    elif self_inbox_filter == 'messages':
        messages = messages.order_by('-created_at')
        data = [{
            'id': m.id, 'message': censored_content(m.message)} 
            for m in messages]
        return JsonResponse({'messages': data})
    
    else:
        questions = questions.order_by('-created_at')
        messages = messages.order_by('-created_at')
        combined = sorted(
            list(questions) + list(messages), 
            key=lambda x: x.created_at, 
            reverse=True
        )
        data = []
        for item in combined:
            if item.question:
                data.append({'id': item.id, 'type': 'question', 'content': censored_content(item.question)})
            else:
                data.append({'id': item.id, 'type': 'message', 'content': censored_content(item.message)})
        return JsonResponse({'inbox': data})
    
