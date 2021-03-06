from django.contrib import admin
from .models import Provincia, Departamento, Localidad

class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'estado']
	ordering = ['nombre']
	search_fields = ['nombre']

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'provincia', 'estado']
	ordering = ['nombre', 'provincia']
	search_fields = ['nombre']
	raw_fields = ['provincia']

class LocalidadAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'codigo_postal', 'departamento', 'estado']
	ordering = ['nombre']
	search_fields = ['nombre']
	raw_fields = ['departamento']

admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Localidad, LocalidadAdmin)
