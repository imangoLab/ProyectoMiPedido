# -*- conding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad
from apps.productos.models import Producto
from apps.negocios.models import Negocio
from apps.personas.models import Persona
from apps.categorias.models import Marca_SubCategoria


DiasType = (
	("lu","Lunes" ),
	("ma","Martes"),
	("mi","Miercoles"),
	("ju","Jueves" ),
	("vi","Viernes"),
	("sa","Sabado"),
	("do","Domingo")
)



class Tipo_Distribuidora (models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

	
class Distribuidora (models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(verbose_name=u"Descripcion")
	numero_contacto = models.PositiveIntegerField(verbose_name=u"Numero de contacto")
	localidad = models.ForeignKey(Localidad, verbose_name=u"Localidad")
	direccion = models.CharField(max_length=50, verbose_name=u"Direccion")
	persona_cargo = models.ForeignKey(Persona, verbose_name=u"Persona a cargo")
	estado = models.BooleanField(default=True)
	
	
class Categoria_Distribuidora (models.Model):
	distribuidora = models.ForeignKey(Distribuidora)
	tipo_distribuidora = models.ForeignKey(Tipo_Distribuidora)
	estado = models.BooleanField(default=True)


class Permiso_Distribuidora (models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	estado = models.BooleanField(default=True)


class Usuario_Distribuidora (models.Model):
	distribuidora = models.ForeignKey(Distribuidora, verbose_name=u"Distribuidora")
	usuario = models.ForeignKey(User, verbose_name=u"Usuario")
	permiso = models.ForeignKey(Permiso_Distribuidora, verbose_name=u"Permiso", blank=True) #por ahora no se manejan permisos
	estado = models.BooleanField(default=True)


class MarcaXSubcategoria_Distribuidora (models.Model):
	distribuidora = models.ForeignKey(Distribuidora)
	marcaSubCategoria = models.ForeignKey(Marca_SubCategoria)
	estado = models.BooleanField(default=True)


class Producto_Distribudora (models.Model):
	distribudora = models.ForeignKey(Distribuidora)
	marcaXSubcategoriaDistribuidora = models.ForeignKey(MarcaXSubcategoria_Distribuidora)
	producto = models.ForeignKey(Producto)
	stock = models.PositiveIntegerField()
	estado = models.BooleanField(default=True)


class Ruta (models.Model):
	distribuidora = models.ForeignKey(Distribuidora)
	nombre = models.CharField(max_length=50)
	recorrido = models.TextField()
	dia = models.CharField(max_length=2, choices=(DiasType))
	estado = models.BooleanField(default=True)


class Negocio_Distribuidora (models.Model):  # Socio
	negocio = models.ForeignKey(Negocio)
	distribuidora = models.ForeignKey(Distribuidora)
	ruta = models.ForeignKey(Ruta, null=True, blank=True)
	alias_distribuidora = models.CharField(max_length=50, blank=True)
	alias_negocio = models.CharField(max_length=50, blank=True)
	estado = models.BooleanField(default=True)
	class Meta:
		unique_together = ("negocio", "distribuidora")

class Anuncio (models.Model):

	def url(self,nombreArchivo):
		ruta = "imagenesAunicios/%s/%s" %(self.id_distribuidora.nombre,str(nombreArchivo))
		return ruta

	distribuidora = models.ForeignKey(Distribuidora)
	imagen = models.ImageField(upload_to=url, blank=True, null=True)
	titulo = models.CharField(max_length=50)
	descripcion = models.TextField()
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo
