# Importacion de render
from django.shortcuts import render

# Asegúrate de tener las importaciones correctas para tus modelos
from .models import Cliente, Venta, Empleado, Area

# Definicion de las vistas de las tablas
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'venta_list.html', {'ventas': ventas})

def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado_list.html', {'empleados': empleados})

def area_list(request):
    areas = Area.objects.all()
    return render(request, 'area_list.html', {'areas': areas})
