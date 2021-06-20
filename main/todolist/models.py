from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class List(models.Model):
    pass

class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, blank=True, null=True)
    task_name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    pub_date = models.DateTimeField("date created", default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.task_name


class CreateForm(forms.Form):
    task_text = forms.CharField(max_length=100, label=False, required=True, \
                                 validators=[MinLengthValidator(3)], \
                                 widget=forms.TextInput(attrs={'placeholders': 'Enter task name...'})
                                )       

    # def clean_task_text(self):
    #     data = self.cleaned_data['task_text']

    #     # if length < 3:
    #     if len(data) < 3:
    #         raise ValidationError('Task name must be more than 3 chars!')

    #     return data