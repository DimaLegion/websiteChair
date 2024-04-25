from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def chair(request):
    return render(request, 'main/chair.html')


def table(request):
    return render(request, 'table.html')


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(create)
        else:
            error = 'Форма заполнена не полность!'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
