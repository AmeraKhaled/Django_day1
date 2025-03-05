from django.shortcuts import render, redirect
from .models import Trainee
from .forms import TraineeForm
    
def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, "trainee/trainee_list.html", {"trainees": trainees})

def add_trainee(request):
    if request.method == "POST":
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("traineelist")  
    else:
        form = TraineeForm()
    return render(request, "trainee/add_trainee.html", {"form": form})
