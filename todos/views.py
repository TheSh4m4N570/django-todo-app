from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from todos.models import Todo

# Create your views here.


def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        if task != "":
            Todo.objects.create(task=task)
            return redirect('home')
        return redirect('home')


def mark_as_completed(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.is_completed = True
    task.save()
    print(task.task)
    return redirect('home')


def mark_as_not_completed(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.is_completed = False
    task.save()
    print(task.task)
    return redirect('home')


def edit_task(request, pk):
    get_task = get_object_or_404(Todo, pk=pk)
    context = {'task': get_task}
    if request.method == 'POST':
        get_task.task = request.POST['task']
        get_task.save()
        return redirect('home')
    return render(request, template_name='edit_task.html', context=context)


def delete_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.delete()
    return redirect('home')