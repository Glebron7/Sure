from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name