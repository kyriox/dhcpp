from django.contrib import admin
from . models import Person, Role, Computer, Localization, MacAdress

class PersonAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email')
    search_fields=['last_name','first_name']

class RoleAdmin(admin.ModelAdmin):
    list_display=('rol_name','description')

class ComputerAdmin(admin.ModelAdmin):
    list_display=('owner','host_name')

# Register your models here.
admin.site.register(Person,PersonAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Localization)
admin.site.register(MacAdress)