
from django.urls import path
from .import views

urlpatterns = [
    path('getemploye/',views.EmployeList, name = 'employes'),
    path('employeadd/', views.Employeadd, name = "add"),
    path('employeupdate/<str:pk>/', views.Employeupdate,name= "update"),
    path('employedelete/<str:pk>/', views.Employedelete,name= "delete"),


]
