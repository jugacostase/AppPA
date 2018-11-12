from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    documento_identidad = models.BigIntegerField()
    fecha_nacimiento = models.DateTimeField()
    universidad = models.CharField(null=True,max_length=30)
    fecha_ten_grado = models.DateTimeField
    correo = models.CharField(primary_key=True, max_length=50)
    talla_camiseta = models.CharField(null=True, max_length=3)
    estado_persona = models.BooleanField()
    rol_persona = models.CharField(max_length=15)

class Reporte(models.Model):
    tablero = models.CharField(max_length=500)
    tarjeta = models.CharField(max_length=500)
    horas_reportadas = models.FloatField()
    fecha_de_reporte = models.DateTimeField()
    observacion = models.CharField(max_length=1000)
    estado = models.CharField(max_length=500)
    correo = models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_Reporte = models.IntegerField(primary_key=True)

class Tarea(models.Model):
    id_tarea = models.CharField(primary_key=True, max_length=500)
    tarjeta = models.CharField(max_length=500)
    tablero = models.CharField(max_length=500)
    estado_tarjeta = models.CharField(max_length=500)
    porcentaje_avance = models.FloatField()



