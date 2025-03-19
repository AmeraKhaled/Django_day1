from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register  # Import your register view
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"  

urlpatterns = [
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),  
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", register, name="register"),  # Your custom register view
]
