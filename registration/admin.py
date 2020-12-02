from django.contrib import admin
from . models import Person, Role, Computer, Localization, MacAdress

class PersonAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email')
    search_fields=['last_name','first_name']


class RoleAdmin(admin.ModelAdmin):
    list_display=('rol_name','description')


class MacInline(admin.TabularInline):
    model = MacAdress
    # Mostramos un inline vacio por defecto
    extra = 1

#class ComputerInline(admin.TabularInline):
#    model = Computer
    # Mostramos un inline vacio por defecto
#    extra = 1

class ComputerAdmin(admin.ModelAdmin):
    list_display=('owner','host_name')
    inlines=[MacInline]

class LocalizationAdmin(admin.ModelAdmin):
    list_display=('name','description')
    #inlines=[ComputerInline]

class MacAdressAdmin(admin.ModelAdmin):
    list_display=('mac','computer')
    search_fields=['computer']

# Register your models here.
admin.site.register(Person,PersonAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Localization, LocalizationAdmin)
admin.site.register(MacAdress, MacAdressAdmin)
