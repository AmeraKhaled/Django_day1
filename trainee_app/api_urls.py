from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import (
    TraineeListCreateAPI, TraineeUpdateDeleteAPI,
    update_track, TrackViewSet
)


router = DefaultRouter()
router.register(r'tracks', TrackViewSet)

urlpatterns = [
    path("trainees/", TraineeListCreateAPI.as_view(), name="api_trainee_list_create"),
    path("trainees/<int:pk>/", TraineeUpdateDeleteAPI.as_view(), name="api_trainee_update_delete"),
    path("tracks/<int:pk>/update/", update_track, name="api_track_update"),
    path("", include(router.urls)), 
]
