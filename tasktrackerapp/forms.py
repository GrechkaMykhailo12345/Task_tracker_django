from django import forms
from tasktrackerapp.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'Всі'),
        ('Full completed!', 'Повністю готово!'),
        ('pending', 'Очікується'),
        ('in_progress', 'В процесі'),
        ('completed', 'Готово!'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус")
