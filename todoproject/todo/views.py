from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title and description:
            Task.objects.create(title=title, description=description)
            # appName = 'todo' so it'll check appName = todo name = task_list in urls.py
            return redirect(reverse('todo:task_list'))
        error = "Both title and description are required."
        return render(request, 'todo/task_form.html', {'error': error})
    return render(request, 'todo/task_form.html')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        completed = request.POST.get('completed') == 'on'
        if title:
            task.title = title
            task.description = description
            task.completed = completed
            task.save()
            return redirect(reverse('todo:task_list'))
        return render(request, 'todo/task_form.html', {'task': task, 'error': "Title is required."})
    return render(request, 'todo/task_form.html', {'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('todo:task_list'))
    return render(request, 'todo/task_confirm_delete.html', {'task': task})
