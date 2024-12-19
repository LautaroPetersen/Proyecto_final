from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import EspacioTrabajo, Proyecto, Tarea
from django.db.models import Q  
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EspacioTrabajoForm, ProyectoForm, TareaForm






# Create your views here.

def inicio(request):
    return render(request, "App/index.html")

# Página "Sobre la aplicación"
def sobre_aplicacion(request):
    return render(request, 'app/sobre_aplicacion.html')

# Página "Sobre mí"
def sobre_mi(request):
    return render(request, 'app/sobre_mi.html')



class DashboardView(LoginRequiredMixin, ListView):
    model = EspacioTrabajo
    template_name = "app/dashboard.html"
    context_object_name = "espacios"

    def get_queryset(self):
        # Mostrar espacios donde el usuario es administrador o colaborador
        usuario = self.request.user
        return EspacioTrabajo.objects.filter(
            Q(administrador=usuario) | Q(colaboradores=usuario)
        ).distinct()
    
class EspacioDetalleView(DetailView):
    model = EspacioTrabajo
    template_name = "app/espacio_detalle.html"
    context_object_name = "espacio"



class CrearEspacioView(LoginRequiredMixin, CreateView):
    model = EspacioTrabajo
    form_class = EspacioTrabajoForm
    template_name = "app/crear_espacio.html"
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        # Asignar automáticamente al administrador
        form.instance.administrador = self.request.user
        return super().form_valid(form)


class CrearProyectoView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "app/crear_proyecto.html"

    def form_valid(self, form):
        # Vincular el proyecto al espacio de trabajo actual
        espacio = EspacioTrabajo.objects.get(pk=self.kwargs['espacio_id'])
        form.instance.espacio = espacio
        return super().form_valid(form)

    def get_success_url(self):
        # Redirige al detalle del espacio después de crear el proyecto
        return reverse_lazy('espacio_detalle', kwargs={'pk': self.kwargs['espacio_id']})

class CrearTareaView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = "app/crear_tarea.html"

    def form_valid(self, form):
        # Vincular la tarea al proyecto actual
        proyecto = Proyecto.objects.get(pk=self.kwargs['proyecto_id'])
        form.instance.proyecto = proyecto
        return super().form_valid(form)

    def get_success_url(self):
        # Redirige al detalle del proyecto después de crear la tarea
        return reverse_lazy('proyecto_detalle', kwargs={'pk': self.kwargs['proyecto_id']})

class ProyectoDetalleView(LoginRequiredMixin, DetailView):
    model = Proyecto
    template_name = "app/proyecto_detalle.html"
    context_object_name = "proyecto"

class EditarTareaView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = "app/editar_tarea.html"

    def get_success_url(self):
        return reverse_lazy('proyecto_detalle', kwargs={'pk': self.object.proyecto.id})
    
class EliminarTareaView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = "app/eliminar_tarea.html"  

    def get_success_url(self):
        return reverse_lazy('proyecto_detalle', kwargs={'pk': self.object.proyecto.id})