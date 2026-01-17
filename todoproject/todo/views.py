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

