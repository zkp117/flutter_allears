from django.shortcuts import render
from rest_framework import viewsets
from .models import QuestionsModel, AnswersModel

class QuestionsModelViewSet(viewsets.ModelViewSet):
    queryset = QuestionsModel.objects.all()
    serializer_class = QuestionsModelSerializer
class AnswersModelViewSet(viewsets.ModelViewSet):
    queryset = AnswersModel.objects.all()
    serializer_class = AnswersModelSerializer