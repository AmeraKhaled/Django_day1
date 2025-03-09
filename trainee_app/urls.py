from django.urls import path
from .views import trainee_list, add_trainee, update_trainee, delete_trainee

urlpatterns = [
    path("list/", trainee_list, name="traineelist"),  
    path("add/", add_trainee, name="add_trainee"), 
    path("<int:id>/update/", update_trainee, name="update_trainee"),
    path("<int:id>/delete/", delete_trainee, name="delete_trainee"),
    
]
