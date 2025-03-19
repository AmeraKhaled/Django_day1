from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect after successful registration
    else:
        form = UserCreationForm()
        
    return render(request, "accounts/register.html", {"form": form})

class CustomLoginView(LoginView):  # Uses Django's built-in login system
    template_name = "accounts/login.html"

class CustomLogoutView(LogoutView):
    next_page = "login"  # Redirect after logout
