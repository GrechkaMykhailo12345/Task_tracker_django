from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Очікується'),
        ('in_progress', 'В процесі'),
        ('completed', 'Готово!'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    ]
    title = models.CharField(max_length=100, verbose_name='Назва:')
    description = models.TextField(null=True, blank=True, verbose_name='Опис:')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Статус:')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium', verbose_name='Пріоритет:')
    due_date = models.DateTimeField(verbose_name='Термін виконання:')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення:')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created', verbose_name='Створено користувачем:')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Завдання"
        verbose_name_plural = "Завдання"