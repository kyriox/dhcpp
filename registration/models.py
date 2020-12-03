from django.db import models
from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe
# Create your models here.

class Role(models.Model):
        rol_name = models.CharField(max_length=128, null=False, blank=False, unique=True)
        description = models.CharField(max_length=128, null=True, blank=True) 
        def __str__(self):
                return self.rol_name

class Localization(models.Model):
        name = models.CharField(max_length=128, null=False, blank=False, unique=True)
        description = models.CharField(max_length=128, null=True, blank=True)
        #def __unicode__():
        #        return f'{self.name}' 

        def __str__(self):
                return self.name


class Person(models.Model):
        first_name  =  models.CharField(max_length=128, null=False, blank=False)
        middle_name  =  models.CharField(max_length=128, null=True, blank=True)
        last_name = models.CharField(max_length=128, null=False, blank=False)
        phone_number = models.CharField(max_length=22,  null=True, blank=True)
        email = models.EmailField(blank=False, null=False, unique=True)
        registration_number = models.CharField(max_length=22, null=False, blank=False, default=None)
        #sex = models.CharField(max_length=1, choices=(('1','F'),('2','M'),('3','O')))
        role = models.ForeignKey(Role,on_delete=models.CASCADE)

        def __str__(self):
                return self.first_name + ' ' + self.last_name

class Computer(models.Model):
        responsable = models.ForeignKey(Person, related_name="person_responsable", on_delete=models.CASCADE, default=None)
        owner = models.ForeignKey(Person, related_name="person_owner", on_delete=models.CASCADE)
        localization = models.ForeignKey(Localization, on_delete=models.CASCADE)
        host_name = models.CharField(max_length=128, null=False, blank=False)
        op_sys = models.CharField(max_length=128, null=False, blank=False, default=None)
        server = models.BooleanField(default=False, verbose_name='It is server?')
        valid = models.BooleanField(default=False)
        def __str__(self):
                return self.host_name

class MacAddress(models.Model):
        mac = models.CharField(max_length = 17, null = False, blank = False)
        computer = models.ForeignKey(Computer, on_delete=models.CASCADE)




