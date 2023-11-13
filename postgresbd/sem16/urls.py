
from django.urls import path
from .views import cliente_list, venta_list, empleado_list, area_list


urlpatterns = [
    path('clientes/', cliente_list, name='cliente_list'),
    path('ventas/', venta_list, name='venta_list'),
    path('empleados/', empleado_list, name='empleado_list'),
    path('areas/', area_list, name='area_list'),
]