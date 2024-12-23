from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class EspacioTrabajo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Espacio")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    administrador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='espacios_administrados')
    colaboradores = models.ManyToManyField(User, related_name='espacios_colaborados', blank=True)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Proyecto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    espacio = models.ForeignKey('EspacioTrabajo', on_delete=models.CASCADE, related_name='proyectos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]

    nombre = models.CharField(max_length=200, verbose_name="Nombre de la Tarea")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE, related_name='tareas')
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tareas_asignadas')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Comentario(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.tarea.nombre}"
