from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    # print(tasks) to see tasks in console
    return render(request, 'task_list.html', {"tasks": tasks})

def create_task(request):
    # print(request.POST) # To see sent data on the console from the web
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    # print(task_id) to see the task id in console
    task = Task.objects.get(pk=task_id) # You can replace "pk" with "id" instead
    task.delete()
    return redirect('/tasks/')
