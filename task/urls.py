from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('myhistory', views.task_history, name='history'),

    path('about/', views.about, name='about'),
    # path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', views.TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update', views.TaskUpdateView.as_view(template_name='task/task_update.html'), name='task-update'),

]

