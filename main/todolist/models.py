from django.db import models
from django.utils import timezone

# Create your models here.

class List(models.Model):
    pass

class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, blank=True, null=True)
    task_name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    pub_date = models.DateTimeField("date created", default=timezone.now)

    def __str__(self) -> str:
        return self.task_name
