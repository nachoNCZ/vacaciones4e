from django.db import models

# Create your models here.
from django.db import models

class Empleado(models.Model):
    nombre           = models.CharField(max_length=100)
    email            = models.EmailField(unique=True)
    fecha_ingreso    = models.DateField()
    dias_disponibles = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

class Vacacion(models.Model):
    empleado        = models.ForeignKey(
                          Empleado,
                          on_delete=models.CASCADE,
                          related_name='vacaciones'
                      )
    fecha_inicio    = models.DateField()
    fecha_fin       = models.DateField()
    dias_solicitados = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.empleado.nombre}: {self.fecha_inicio} → {self.fecha_fin}"

class Permiso(models.Model):
    empleado     = models.ForeignKey(
                       Empleado,
                       on_delete=models.CASCADE,
                       related_name='permisos'
                   )
    TIPO_CHOICES = [
        ('Personal', 'Personal'),
        ('Médico',    'Médico'),
        ('Otro',      'Otro'),
    ]
    tipo          = models.CharField(max_length=20, choices=TIPO_CHOICES)
    fecha         = models.DateField()
    hora_inicio   = models.TimeField()
    hora_fin      = models.TimeField()

    def __str__(self):
        return f"{self.empleado.nombre} – {self.tipo} ({self.fecha})"

class Aniversario(models.Model):
    empleado = models.ForeignKey(
                   Empleado,
                   on_delete=models.CASCADE,
                   related_name='aniversarios'
               )
    fecha    = models.DateField()

    def __str__(self):
        return f"Aniversario: {self.empleado.nombre} el {self.fecha}"
