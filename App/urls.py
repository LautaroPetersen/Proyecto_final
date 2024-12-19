from django.urls import path
from App import views
from .views import DashboardView, EspacioDetalleView, CrearEspacioView, CrearProyectoView, CrearTareaView, ProyectoDetalleView, EditarTareaView, EliminarTareaView 

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('sobre-aplicacion/', views.sobre_aplicacion, name='sobre_aplicacion'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('espacios/<int:pk>/', views.EspacioDetalleView.as_view(), name='espacio_detalle'),
    path('espacios/nuevo/', CrearEspacioView.as_view(), name='crear_espacio'),
    path('espacios/<int:espacio_id>/proyectos/nuevo/', CrearProyectoView.as_view(), name='crear_proyecto'),
    path('proyectos/<int:proyecto_id>/tareas/nueva/', CrearTareaView.as_view(), name='crear_tarea'),
    path('proyectos/<int:pk>/', ProyectoDetalleView.as_view(), name='proyecto_detalle'),
    path('tareas/<int:pk>/editar/', EditarTareaView.as_view(), name='editar_tarea'),
    path('tareas/<int:pk>/eliminar/', EliminarTareaView.as_view(), name='eliminar_tarea'),

]
