import os
from django.urls import path, include

urlpatterns = [
    path('', include('users.api.urls')),
]
