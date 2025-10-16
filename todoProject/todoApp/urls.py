from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:pk>/update/', views.update_task, name='update_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
]