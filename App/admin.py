from django.contrib import admin
from .models import EspacioTrabajo, Proyecto, Tarea
# Register your models here.

@admin.register(EspacioTrabajo)
class EspacioTrabajoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'administrador')
    filter_horizontal = ('colaboradores',)



@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'espacio', 'fecha_creacion')

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proyecto', 'estado', 'fecha_vencimiento', 'asignado_a')
    list_filter = ('estado', 'proyecto')
    search_fields = ('nombre',)