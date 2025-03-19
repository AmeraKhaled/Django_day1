from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render 

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path("", home, name="home"),  

    path("admin/", admin.site.urls),
    path('api/', include('trainee_app.api_urls')),  
    path("trainee/", include("trainee_app.urls")), 
    path("course/", include("course_app.urls")), 
    path("accounts/", include("accounts.urls")),
    

]
