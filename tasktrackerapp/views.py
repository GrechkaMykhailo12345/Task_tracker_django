from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from tasktrackerapp.forms import TaskForm
from tasktrackerapp.models import Task

class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"

class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"

class TaskCreateView(CreateView):
    model = Task
    template_name = "task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasktrackerapp:task_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)