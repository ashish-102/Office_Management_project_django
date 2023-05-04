from django.db import models

# Create your models here.

# dapartments in the company
class Department(models.Model):
    name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.location}'
    

# rols in the company
class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
    

# table for employees details
class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.IntegerField()
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    hireDate = models.DateField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


    