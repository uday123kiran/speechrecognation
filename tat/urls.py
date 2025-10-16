
from django.urls import path
from . import views

urlpatterns = [
    path("", views.jarvis, name="home"),      # http://127.0.0.1:8000/
    path("jarvis/", views.jarvis, name="jarvis"),  # http://127.0.0.1:8000/jarvis/
]
