from django.contrib import admin
from django.urls import path, include
from trainee_app.views import trainee_list  
from django.shortcuts import render 

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path("", home, name="home"),  

    path("admin/", admin.site.urls),
    path("trainee/", include("trainee_app.urls")), 
    path("course/", include("course_app.urls")),  
]
