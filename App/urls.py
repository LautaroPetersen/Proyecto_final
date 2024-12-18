from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('sobre-aplicacion/', views.sobre_aplicacion, name='sobre_aplicacion'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
]