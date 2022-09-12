from django.db import models
from projects.models import Project
from django.conf import settings

User_model = settings.AUTH_USER_MODEL


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(null=True)
    project = models.ForeignKey(
        Project, related_name="tasks", on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        User_model, null=True, related_name="tasks", on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
