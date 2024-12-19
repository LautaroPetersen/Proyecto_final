from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Avatar


class UserEditForm(UserChangeForm):

    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']
        # help_texts = {k:"" for k in fields} 



class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']  # Solo permitimos subir la imagen
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }