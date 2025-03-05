from django.urls import path
from .views import trainee_list, add_trainee 

urlpatterns = [
    path("list/", trainee_list, name="traineelist"),  
    path("add/", add_trainee, name="add_trainee"), 
]
