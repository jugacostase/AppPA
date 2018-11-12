from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Persona, Reporte, Tarea
admin.site.register(Persona)
admin.site.register(Reporte)
admin.site.register(Tarea)