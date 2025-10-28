from django.db import models

class Resultado(models.Model):
    id_resultado = models.AutoField(primary_key=True)
    cod_ingreso = models.ForeignKey(
        'APIPaciente.Pacientes',       # modelo destino
        on_delete=models.CASCADE,      # qué pasa si se borra el ingreso
        db_column='cod_ingreso'        # nombre de la columna en la BD
    )
    hdl = models.CharField(max_length=255)
    ldl = models.CharField(max_length=255)
    trigliceridos = models.CharField(max_length=255)
    cod_laboratorista = models.ForeignKey(
        'APILaboratoristas.Laboratoristas',               # modelo destino
        on_delete=models.SET_NULL,     # si se borra, deja el valor en NULL
        null=True,
        db_column='cod_laboratorista'
    )
    
    class Meta:
        db_table = 'Resultados'
