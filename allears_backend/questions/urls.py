from django.urls import path, include

urlpatterns = [
    path('', include('questions.api.urls')),
]
