from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import List, Task
from django.urls import reverse

# Create your views here.


def index(request):
    tasks = Task.objects.order_by("-pub_date")
    return render(request, "todolist/main.html", {'tasks': tasks})

def delete(r, task_id):
    t = get_object_or_404(Task, pk=task_id)
    t.delete()
    return HttpResponseRedirect(reverse("todolist:index"))

def update_page(r, task_id):
    t = get_object_or_404(Task, pk=task_id)
    return render(r, "todolist/update.html", {"task": t})

def update(r, task_id):
    t = get_object_or_404(Task, pk=task_id)
    return HttpResponseRedirect(reverse("todolist:index"))

def create_page(r):
    return render(r, "todolist/create.html")

def create(r):
    if r.method == "POST":
        t = Task()
        t.task_name = r.POST['task_name']
        t.save()

    return HttpResponseRedirect(reverse("todolist:index"))