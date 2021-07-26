from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('agents/', views.agents, name='agents'),
    path('tasks/', views.tasks, name='tasks'),
    path('task/details/<int:id>', views.details, name='details'),
    path('proceed_auth/', views.proceed_auth, name="proceed_auth"),
    path('proceed_logout/', views.proceed_logout, name="proceed_logout"),
    path('main/', views.main_page, name='main'),
    path('task_in_work/<int:id>', views.task_in_work, name='task_in_work'),
    path('create_task/', views.create_task, name='create_task'),
]