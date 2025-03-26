from django.db import models
from tasks.models import Task  # Importamos el modelo Task

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    tasks = models.ManyToManyField(Task, related_name="categories")  # Relación con Task

    def __str__(self):
        return self.name
