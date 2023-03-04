from django.urls import path
from todo_app import views

urlpatterns = [
    path('api/todo-lists', views.todolists_handler),
    path('api/todo-lists/<int:pk>', views.todolist_handler),
    path('api/todo-lists/<int:pk>/todos', views.todolist_todos_handler),
    path('todos', views.todos_handler),
    path('todos/<int:pk>', views.todo_handler)
]