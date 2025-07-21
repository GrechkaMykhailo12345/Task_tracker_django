from django.contrib import admin
from django.urls import include, path

from tasktrackerapp.views import TaskListView, TaskDetailView, TaskCreateView

urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('task/<int:pk>/detail', TaskDetailView.as_view(), name="task_detail"),
    path('task_create', TaskCreateView.as_view(), name="task_create"),
]

app_name = "tasktrackerapp"