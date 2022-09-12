from django.urls import path
from projects.views import ProjectsListView, ProjectDetailView

urlpatterns = [
    path("", ProjectsListView.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
]
