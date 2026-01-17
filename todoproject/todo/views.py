from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})