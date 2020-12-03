from registration.models import Person
from django.forms import ModelForm
from .models import *

class PersonForm(ModelForm):
        class Meta:
                model=Person
                fields='__all__'
                #exclude = ('role',) 

class MacAddressForm(ModelForm):
        class Meta:
                model=MacAddress
                fields='__all__'

class ComputerForm(ModelForm):
        mac_list=forms.CharField(required=True, help_text="Intoduce una lista de macs una por linea",
                                widget=forms.Textarea(attrs={'cols':32,'rows':3}))
        class Meta:
                model=Computer
                fields='__all__'
                exclude = ('valid',)
         
