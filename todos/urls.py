from django.urls import path
from . import views

urlpatterns = [
    path('addtask', views.add_task, name='addtask'),
    path('mark_as_completed/<int:pk>/', views.mark_as_completed, name='mark_as_completed'),
    path('mark_as_not_completed/<int:pk>/', views.mark_as_not_completed, name='mark_as_not_completed'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]