from django.views.generic import ListView, DetailView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectsListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"
