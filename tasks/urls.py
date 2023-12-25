from django.urls import path
from .views import task_list, create_task, delete_task

urlpatterns = [
    path('', task_list),
    path('new_task/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task')
]
