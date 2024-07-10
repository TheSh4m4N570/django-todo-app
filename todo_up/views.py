from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Todo


def home(request):
    todos = Todo.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks = Todo.objects.filter(is_completed=True).order_by('-created_at')
    context = {'todos': todos, 'completed_tasks': completed_tasks}
    return render(request, template_name="home.html", context=context)


