from rest_framework import serializers
from .models import QuestionsModel, AnswersModel

class QuestionsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsModel
        created_at = serializers.DateTimeField(auto_now_add=True)
        fields = ['avatar','user', 'name', 'question',]


class AnswersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswersModel
        fields = ['avatar', 'user', 'name', 'content', 'answered_at']
