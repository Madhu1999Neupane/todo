from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank = True)
    priority = models.IntegerField(default=0,null=True, blank=True) # 0-3 for urgent to not urgent
    is_complete = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True,null=True)
    updated_at = models.DateTimeField(auto_now = True)
    due_date =  models.DateTimeField(blank = True, null = True)
    owner = models.ForeignKey(User, related_name = 'tasks', on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.title