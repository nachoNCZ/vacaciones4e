from django.contrib import admin
from .models import Empleado, Vacacion, Permiso, Aniversario

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Vacacion)
admin.site.register(Permiso)
admin.site.register(Aniversario)