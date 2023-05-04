from django.contrib import admin
from .models import Department, Role, Employee 
# Register your models here.

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'phone' ,'salary', 'dept', 'hireDate')
    