from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
  
"""
task_headers = ['name','desc', 'start_date', 'end_date', 'actual_end_date', 'status', 'comments']

task_data = [
    {'name':'Task 1',
    'desc':'this is a desc',
    'start_date':'02-10-2023',
    'end_date':'05-10-2023',
    'actual_end_date':'NA',
    'status':'',
    'comments':''
    },
    {'name':'Task 2',
    'desc':'this is a desc',
    'start_date':'02-10-2023',
    'end_date':'05-10-2023',
    'actual_end_date':'NA',
    'status':'',
    'comments':''
    }

] 
"""


# Create your models here.
class Task(models.Model):
    status_choices = (
        ("ongoing", "ONGOING"),
        ("completed", "COMPLETED"),
        ("closed", "CLOSED"),
    )

    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=status_choices, default="ongoing")
    comments = models.TextField(blank=True)
    date_cc = models.DateTimeField(auto_now=True)
    # date_cc = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} - {self.creator.username}"
    

    def get_absolute_url(self):
        return reverse("home")
    
