from django.shortcuts import  render, get_object_or_404, redirect
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

def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == "POST":
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect("traineelist") 
    else:
        form = TraineeForm(instance=trainee)  
    return render(request, "trainee/update_trainee.html", {"form": form})

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == "POST":
        trainee.delete()
        return redirect("traineelist")
    return render(request, "course/delete_trainee.html", {"trainee": trainee})
    
    