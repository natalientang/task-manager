from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Task(models.Model):
    name = models.CharField(max_length=200)
    notes = models.TextField(null=True)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        User, related_name="tasks", on_delete=models.CASCADE, null=True
    )
