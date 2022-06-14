from django.db import models

SEXOS = [
    ('F', 'Femenino'),
    ('M', 'Masculino')
]
class Alumno(models.Model):
    carnet = models.CharField(max_length=7, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=SEXOS)
    materia_ganada = models.IntegerField()
    class Meta:
        db_table = 'alumno'
class Materia(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    unidad_valorativa = models.CharField(max_length=1)
    class Meta:
        db_table = 'materia'
class Nota(models.Model):
    alumno = models.ForeignKey(to=Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(to=Materia, on_delete=models.CASCADE)
    ciclo = models.CharField(max_length=6)
    nota_final = models.FloatField()
    class Meta:
        db_table = 'nota'
