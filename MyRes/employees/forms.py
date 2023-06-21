from django import forms
from .models import Employee, Task


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('employee', 'title', 'description')