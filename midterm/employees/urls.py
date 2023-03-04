from django.urls import path
from employees import views

urlpatterns = [
    path('api/employees', views.employees_handler),
    path('api/employees/<int:pk>', views.employee_handler)
]