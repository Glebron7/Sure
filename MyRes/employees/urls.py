from django.urls import path
from . import views
from employees.views import employee_list, employee_detail, employee_add, employee_edit, employee_delete

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
    path('new/', views.employee_new, name='employee_new'),
    path('<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('<int:pk>/task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('', employee_list, name='employee_list'),
    path('employee/<int:pk>/', employee_detail, name='employee_detail'),
    path('employee/add/', employee_add, name='employee_add'),
    path('employee/<int:pk>/edit/', employee_edit, name='employee_edit'),
    path('employee/<int:pk>/delete/', employee_delete, name='employee_delete'),
]