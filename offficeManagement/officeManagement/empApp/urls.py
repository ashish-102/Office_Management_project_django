from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allEmp/', views.allEmp, name='allemps'),
    path('addEmp/', views.addEmp, name='addEmp'),
    path('findEmp/', views.findEmp, name='find'),
    path('rmEmp/', views.rmEmp, name='rm'),
    path('updEmp/<int:pk>/<int:status>', views.updEmp, name='upEmp'),
    path('delEmp/<int:uid>/', views.delEmp, name='delEmp'),
    path('dataUpEmp/<int:id>/', views.dataUpEmp, name='dataUp'),
]