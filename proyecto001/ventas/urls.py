from django.urls import path
from . import views

urlpatterns = [
    path('', views.realizarVentas_view, name="realizar_ventas"),
    path('ventas/', views.ventas_view, name="ventas"),
    path('productos/', views.productos_view, name="productos"),
    path('registrar/', views.agregar),
    path('proforma/', views.emitir_proforma, name="proforma"),  
    path('eliminar_productos/', views.eliminar_productos, name='eliminar_productos'),
]