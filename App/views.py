from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import EspacioTrabajo, Proyecto, Tarea
from django.db.models import Q  
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EspacioTrabajoForm, ProyectoForm, TareaForm,AgregarColaboradorPorUsuarioForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User





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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        proyecto = Proyecto.objects.get(pk=self.kwargs['proyecto_id'])
        kwargs['proyecto'] = proyecto  # Pasa el proyecto al formulario
        return kwargs

    def form_valid(self, form):
        # Asigna el proyecto al que pertenece la tarea
        proyecto = Proyecto.objects.get(pk=self.kwargs['proyecto_id'])
        form.instance.proyecto = proyecto  # Relacionar la tarea con el proyecto
        return super().form_valid(form)

    def get_success_url(self):
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
    
class AgregarColaboradorPorUsuarioView(LoginRequiredMixin, FormView):
    template_name = "app/agregar_colaborador_manual.html"
    form_class = AgregarColaboradorPorUsuarioForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['espacio_id'] = self.kwargs['espacio_id']  # Pasar espacio_id al contexto
        return context

    def form_valid(self, form):
        espacio = EspacioTrabajo.objects.get(pk=self.kwargs['espacio_id'])
        username = form.cleaned_data['username']
        colaborador = User.objects.get(username=username)

        # Verifica que el usuario no esté ya en el espacio
        if colaborador in espacio.colaboradores.all():
            form.add_error('username', "Este usuario ya es colaborador de este espacio.")
            return self.form_invalid(form)

        # Agregar colaborador al espacio
        espacio.colaboradores.add(colaborador)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('espacio_detalle', kwargs={'pk': self.kwargs['espacio_id']})

