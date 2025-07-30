from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tasktrackerapp.models import Task

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логін:', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    username = forms.CharField(label='Логін:', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

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
