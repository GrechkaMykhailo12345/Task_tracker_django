from django.contrib import admin
from django.urls import include, path

from tasktrackerapp.views import TaskListView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name="task_listt"),
    path('task/<int:pk>/detail', TaskDetailView.as_view(), name="task_detail"),
]