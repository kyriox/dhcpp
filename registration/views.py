from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import PersonForm 
from django.shortcuts import redirect
from django import forms
from .models import *
from .forms  import *


# Create your views here.

def hello(request):
    contexto={'title':"Prueba", 'header':"Registro"}
    lista=[{'rol_name':"rol 1", "description":"El rol numero 1"},
           {'rol_name':"rol 2", "description":"El rol numero 2"},
    ]
    contexto['lista']=lista
    person_form=PersonForm(request.POST)
    if person_form.is_valid():
       post = person_form.save(commit=False)
       post.rol_name = "Alumno"
       post.save()
    contexto['formulario']=person_form
    return render(request, 'registration/test.html', contexto)

def regComputer(request):
       computerForm=ComputerForm()
       computerForm.fields['responsable'].queryset=Person.objects.filter(role__rol_name="Responsable").all()
       return render(request, 'registration/register.html',{'form':computerForm})

def regComputerPost(request):
   if request.method == 'POST':
      computerForm=ComputerForm(request.POST)
      computer=computerForm.save()
      macs=request.POST['mac_list']
      for mac in macs.split('\n'):
         mac_object=MacAddress(**{'mac':mac,'computer':computer})
         mac_object.save()
   return HttpResponse(computerForm)

class FormPersonView(HttpRequest):
    def index(request):
       person = PersonForm()
       return render(request, "PersonIndex.html", {"form":person})

    def procesar_formulario(request):
       person = PersonForm(request.POST)
       if person.is_valid():
          #person.rol_id = 1
          person.save()
          person = PersonForm()

       return render(request, "PersonIndex.html", {"form":person, "mensaje": 'OK'})
       #pip install django-crispy-forms
