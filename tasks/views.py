from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from django.urls import reverse_lazy


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.assignee = self.request.user
        item.save()
        return redirect("projects/detail.html")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/mine.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/mine.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
