from django.contrib import admin
from ventas.models import Usuario, Productos, venta

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display= ('codigo', 'nombre', 'usuario', 'contraseña')
    search_fields = ['codigo']
    filter_horizontal= ()
    list_filter=()
    fields =()

admin.site.register(Usuario, UsuarioAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display= ('codigo', 'descripcion', 'stock', 'precio')
    search_fields = ['codigo', 'descripcion']
    filter_horizontal= ()
    list_filter=()
    fields =()

admin.site.register(Productos, ProductoAdmin)

class RegistroAdmin(admin.ModelAdmin):
    list_display= ('codigo', 'producto', 'cantidad', 'PrecioUnitario', 'total')
    search_fields = ['codigo', 'producto']
    filter_horizontal= ()
    list_filter=()
    fields =()

admin.site.register(venta, RegistroAdmin)
