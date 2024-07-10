from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Todos


def home(request):
    todos = Todos.objects.filter(completed=False)
    context = {'todos': todos}
    return render(request, template_name="home.html", context=context)


