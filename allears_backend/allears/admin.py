from django.contrib import admin
from .models import QuestionsModel, AnswersModel
@admin.register(QuestionsModel)
class QuestionsModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)
@admin.register(AnswersModel)
class AnswersModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_text')
    search_fields = ('answer_text',)
    list_filter = ('question',)