from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "show_my_tasks": tasks,
    }
    return render(request, "tasks/mine.html", context)


def edit_tasks(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm(instance=task)
    context = {
        "task_object": task,
        "task_form": form,
    }
    return render(request, "tasks/edit.html", context)
