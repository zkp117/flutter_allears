from django.db import models
from django.contrib.auth.models import User

class QuestionsModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class AnswersModel(models.Model):
    question = models.ForeignKey(QuestionsModel, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return f"{User} {self.question.name}"

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

