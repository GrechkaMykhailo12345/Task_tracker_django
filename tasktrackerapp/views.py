from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tasktrackerapp.models import Task

class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"

class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"