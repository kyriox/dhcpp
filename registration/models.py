from django.db import models
from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe
# Create your models here.

class Role(models.Model):
        rol_name = models.CharField(max_length=128, null=False, blank=False, unique=True)
        description = models.CharField(max_length=128, null=True, blank=True)

        def __unicode__():
                return f'{self.rol_name}' 

class Person(models.Model):
        first_name  =  models.CharField(max_length=128, null=False, blank=False)
        middle_name  =  models.CharField(max_length=128, null=True, blank=True)
        last_name = models.CharField(max_length=128, null=False, blank=False)
        phone_number = models.CharField(max_length=22,  null=True, blank=True)
        email = models.EmailField(blank=False, null=False, unique=True)
        sex = models.CharField(max_length=1, choices=(('1','F'),('2','M'),('3','O')))
        role = models.ForeignKey(Role,on_delete=models.CASCADE)

           
        
