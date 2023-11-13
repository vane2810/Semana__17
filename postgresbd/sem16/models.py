from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    DUI = models.IntegerField()


class Area(models.Model):
    nombre_del_area = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)

    
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    areaid = models.ForeignKey(Area,on_delete=models.CASCADE)


class Venta(models.Model):
    fecha_venta = models.DateTimeField()
    monto = models.FloatField()
    clienteid = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    empleadoid = models.ForeignKey(Empleado,on_delete=models.CASCADE)

