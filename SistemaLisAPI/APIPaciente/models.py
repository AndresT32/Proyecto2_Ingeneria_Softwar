from django.db import models

class Pacientes(models.Model):
    cod_ingreso = models.CharField(primary_key=True, max_length=500)
    documento = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'Pacientes'
