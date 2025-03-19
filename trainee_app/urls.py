from django.urls import path
from .views import TraineeListView, TraineeDeleteView, TraineeCreateView, TraineeUpdateView



urlpatterns = [
    path("", TraineeListView.as_view(), name="traineelist"),
    # path("<int:pk>/", TraineeDetailView.as_view(), name="trainee_detail"),
    path("<int:pk>/delete/", TraineeDeleteView.as_view(), name="trainee_delete"),
    path("create/", TraineeCreateView.as_view(), name="trainee_create"),
    path("<int:pk>/update/", TraineeUpdateView.as_view(), name="trainee_update"),
]
