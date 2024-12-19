from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='Inicio'), name='logout'),
    path('editar_perfil/', views.editar_perfil, name='EditarPerfil'),
    path('cambiar_pass/', views.CambiarPassVeiw.as_view(), name='CambiarPass'),
    path('agregar_avatar', views.agregar_avatar, name="AgregarAvatar"),
]
