from django.core import exceptions
from django.http.response import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import List, Task, CreateForm
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import sys
import json
# Create your views here.


@login_required(login_url='/login')
def index(request):
    form = CreateForm()
    # tasks = request.user.task_set
    tasks = Task.objects.filter(user=request.user).order_by("-pub_date")
    return render(request, "todolist/main.html", {'tasks': tasks, 'form': form})


# delete for ajax
def delete(r, task_id):
    try:
        t = Task.objects.get(pk=task_id)
        t.delete()
        loads = {'task_name': t.task_name}
        # return HttpResponse(json.dumps(loads), content_type="application/json")

        return JsonResponse(loads, status=200)

    except ObjectDoesNotExist:
        return JsonResponse({'error': "object not found", 'task_name': t.task_name }, status=404)

# def update_page(r, task_id)
#     t = get_object_or_404(Task, pk=task_id)
#     return render(r, "todolist/update.html", {"task": t})

def update(r, task_id):
    task_name = r.POST['task_name']
    print(task_name, file=sys.stderr)
    try:
        t = Task.objects.get(pk=task_id)
        t.task_name = task_name
        t.save()
        return HttpResponse(f'{task_name}')
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Can not update")

def create_page(r):
    return render(r, "todolist/create.html")

def create(r):
    if r.method == "POST":
        form = CreateForm(r.POST)
        if form.is_valid():
            t = Task()
            t.task_name = form.cleaned_data['task_text']
            t.save()
            return HttpResponseRedirect(reverse("todolist:index"))
    
    else:
        form = CreateForm()

    tasks = Task.objects.order_by("-pub_date")
    return render(r, "todolist/main.html", {'tasks': tasks, 'form': form})

    

