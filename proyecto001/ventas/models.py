from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Usuario(models.Model):
    codigo = models.CharField(max_length=200, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.CharField(max_length=200, null=True, blank=True)
    contraseña = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name='usuario'
        verbose_name_plural='Usuarios'
    
    def __str__(self):
        return self.nombre



class Productos(models.Model):
    codigo = models.CharField(max_length=200, unique=False, null=True, blank=True)
    descripcion = models.CharField(max_length=200, unique=False, null=True, blank=True)
    stock = models.IntegerField()
    precio = models.IntegerField()

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        order_with_respect_to='descripcion'
    
    def __str__(self):
        return self.descripcion
    

class venta(models.Model):
    codigo = models.CharField(max_length=200, unique=False, null=True, blank=True)
    producto = models.CharField(max_length=200, unique=False, null=True, blank=True)
    cantidad = models.IntegerField()
    PrecioUnitario = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        verbose_name='venta'
        verbose_name_plural ='ventas'
    def __str__(self):
        return self.producto
