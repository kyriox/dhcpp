from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import PersonForm 
from django.shortcuts import redirect
from django import forms

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