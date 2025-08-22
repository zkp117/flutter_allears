from django.urls import path, include

urlpatterns = [
    path('', include('answers.api.urls')),
]
