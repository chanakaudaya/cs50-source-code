from django.urls import path
from . import views
from lecture3 import tasks

app_name = tasks

urlpatterns = [
    path("", views.index, name="index"),
    path("/add", views.tasks, name="tasks")
]