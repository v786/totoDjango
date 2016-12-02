from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Task

def index(request):
    latest_task_list = Task.objects.order_by('-pub_date')[:5]
    context = {'latest_task_list': latest_task_list}
    return render(request, 'tasks/index.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {'task': task})

def results(request, task_id):
    response = "You're looking at the status of task %s."
    return HttpResponse(response % task_id)

def vote(request, task_id):
    return HttpResponse("You're making the status of task : %s." % status_id)