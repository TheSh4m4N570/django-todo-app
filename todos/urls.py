from django.urls import path
from . import views

urlpatterns = [
    path('addtask/', views.add_task, name='addtask')
]