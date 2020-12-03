from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('computer', views.regComputer),
    path('computer/post', views.regComputerPost),
    path('formulario/', views.FormPersonView),
    path('registerPerson/', views.FormPersonView.index, name='registerPerson'),
    path('savePerson/', views.FormPersonView.procesar_formulario, name='savePerson'),
]
