from django.forms import ModelForm
from projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
            "assignee",
            "start_date",
            "due_date",
            "is_completed",
        ]
