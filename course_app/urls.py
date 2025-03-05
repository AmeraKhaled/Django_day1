from django.urls import path
from . import views
from .views import course_list, add_course, update_course, delete_course

urlpatterns = [
    path("list/", course_list, name="course_list"),
    path("add/", views.add_course, name="add_course"),
    path("<int:id>/update/", views.update_course, name="update_course"),
    path("<int:id>/delete/", views.delete_course, name="delete_course"),
]
