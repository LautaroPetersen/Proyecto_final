from django import forms
from .models import EspacioTrabajo, Proyecto, Tarea, Comentario
from django.contrib.auth.models import User

class EspacioTrabajoForm(forms.ModelForm):
    class Meta:
        model = EspacioTrabajo
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Espacio'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
        }


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Proyecto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
        }

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'estado', 'asignado_a', 'fecha_vencimiento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Tarea'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'asignado_a': forms.Select(attrs={'class': 'form-select'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.proyecto = kwargs.pop('proyecto', None)  # Recibe el proyecto en el constructor
        super().__init__(*args, **kwargs)
        if self.proyecto:
            # Filtra los usuarios que son colaboradores del espacio del proyecto
            self.fields['asignado_a'].queryset = self.proyecto.espacio.colaboradores.all()

    def clean_asignado_a(self):
        asignado_a = self.cleaned_data.get('asignado_a')
        if asignado_a and self.proyecto and asignado_a not in self.proyecto.espacio.colaboradores.all():
            raise forms.ValidationError("El usuario seleccionado no es colaborador de este espacio.")
        return asignado_a



class AgregarColaboradorPorUsuarioForm(forms.Form):

    username = forms.CharField(
        label="Nombre de Usuario",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre de usuario'}),
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("El usuario ingresado no existe.")
        return username
    
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe tu comentario aquí...'
            }),
        }
        labels = {
            'texto': 'Comentario'
        }