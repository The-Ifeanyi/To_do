from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks=["food","play","read"]
def index(request):
    return render(request,"tasks/index.html",{
        "tasks":tasks

    })

class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")

def add_task(request):
    if request.method == "POST":
        form= NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasks.append(task)

            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{
                "forms": form
            })

    return render(request,"tasks/add.html",{
        "form":NewTaskForm()
    })




# Create your views here.
