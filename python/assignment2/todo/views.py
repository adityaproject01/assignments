from django.http import HttpResponse
from .models import Task

def list_tasks(request):
    tasks = Task.objects.all()
    task_list = '\n'.join([task.title for task in tasks])
    return HttpResponse(task_list)

def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return HttpResponse(f'Task "{task.title}" marked as complete.')
