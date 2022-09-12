from django.shortcuts import render
from django.views.generic import ListView
from projects.models import Project


class ProjectsListView(ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projects"
