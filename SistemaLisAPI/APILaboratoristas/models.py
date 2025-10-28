from django.db import models

class Laboratoristas(models.Model):
    cod_laboratorista = models.CharField(primary_key=True, max_length=500)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    profesion = models.CharField(max_length=100)

    class Meta:
        db_table = 'Laboratoristas'
