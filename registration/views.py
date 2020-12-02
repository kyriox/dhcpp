from django.shortcuts import render
from django.http import HttpResponse
from .models import * #PersonForm, ComputerForm, MacAdressForm 

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

def regComputer(request):
       computerForm=ComputerForm()
       computerForm.fields['owner'].queryset=Person.objects.filter(role__description="Responsable").all()
       return render(request, 'registration/register.html',{'form': computerForm})