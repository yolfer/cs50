from django import forms
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

tasks = ["foo", "bar", "baz"] #TODO sessions

# Does client-side validation, but not server (see add() method below)
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        # server-side validation
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form":form
            })
  
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
