from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasktrackerapp import models
from tasktrackerapp.mixins import UserIsOwnerMixin
from tasktrackerapp.forms import TaskForm, TaskFilterForm
from tasktrackerapp.models import Task
from django.http import HttpResponseRedirect

class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status", "")
        if status:
            queryset = queryset.filter(status=status)
        return queryset
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskFilterForm(self.request.GET)
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasktrackerapp:task_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskCompleteView(LoginRequiredMixin, UserIsOwnerMixin, View):
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = "Full completed!"
        task.save()
        return HttpResponseRedirect(reverse_lazy("tasktrackerapp:task_list"))
    
    def get_object(self):
        task_id = self.kwargs.get("pk")
        return get_object_or_404(models.Task, pk=task_id)

class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_update_form.html"
    success_url = reverse_lazy("tasktrackerapp:task_list")

class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    template_name = "task_delete_confirmation.html"
    success_url = reverse_lazy("tasktrackerapp:task_list")