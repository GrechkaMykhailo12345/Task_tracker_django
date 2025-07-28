from django.contrib import admin
from django.urls import include, path

from tasktrackerapp.views import TaskListView, TaskDetailView, TaskCreateView, TaskCompleteView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('task/<int:pk>/detail', TaskDetailView.as_view(), name="task_detail"),
    path('task_create', TaskCreateView.as_view(), name="task_create"),
    path('task/<int:pk>/complete', TaskCompleteView.as_view(), name="task_complete"),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name="task_update"),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name="task_delete"),
]

app_name = "tasktrackerapp"