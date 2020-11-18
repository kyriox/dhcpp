from django.shortcuts import render
from django.http import HttpResponse
from .models import PersonForm 

# Create your views here.

def hello(request):
    contexto={'title':"Prueba", 'header':"Un ecabezado"}
    lista=[{'rol_name':"rol 1", "description":"El rol numero 1"},
           {'rol_name':"rol 2", "description":"El rol numero 2"},
    ]
    contexto['lista']=lista
    person_form=PersonForm()
    contexto['formulario']=person_form
    return render(request, 'registration/test.html', contexto)
