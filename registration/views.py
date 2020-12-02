from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
from .models import * #PersonForm, ComputerForm, MacAdressForm 
=======
from django.http import HttpResponse, HttpRequest
from .forms import PersonForm 
from django.shortcuts import redirect
from django import forms
>>>>>>> e82bc1482c78d51ebd240920426b4cfe1a3bcdbb

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
<<<<<<< HEAD

def regComputer(request):
       computerForm=ComputerForm()
       computerForm.fields['owner'].queryset=Person.objects.filter(role__description="Responsable").all()
       return render(request, 'registration/register.html',{'form': computerForm})
=======
 
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
>>>>>>> e82bc1482c78d51ebd240920426b4cfe1a3bcdbb
