from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, AvatarFormulario
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.views import PasswordChangeView  
from django.urls import reverse_lazy  
from django.contrib.auth.models import User
from .models import Avatar

# Create your views here.


def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})


@login_required
def editar_perfil(request):

   
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)

        if miFormulario.is_valid():

            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.avatar.save()

            miFormulario.save()

            # Retornamos al inicio una vez guardado los datos
            return render(request, "App/index.html")

    else:
        miFormulario = UserEditForm(instance=request.user)

    return render(
        request,
        "usuarios/editar_usuario.html",
        {
            "mi_form": miFormulario,
            "usuario": usuario
        }
    )

class CambiarPassVeiw(LoginRequiredMixin, PasswordChangeView):
    template_name = "usuarios/cambiar_contrasenia.html"
    success_url = reverse_lazy('EditarPerfil')


@login_required
def agregar_avatar(request):
    if request.method == "POST":
        mi_form = AvatarFormulario(request.POST, request.FILES)
        if mi_form.is_valid():
            # Eliminar el avatar anterior si existe
            Avatar.objects.filter(user=request.user).delete()

            # Crear un nuevo avatar
            avatar = Avatar(user=request.user, imagen=mi_form.cleaned_data['imagen'])
            avatar.save()
            return redirect('dashboard')  # Redirigir al dashboard u otra vista
    else:
        mi_form = AvatarFormulario()

    return render(request, "usuarios/agregar_avatar.html", {"mi_form": mi_form})