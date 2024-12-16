from django.urls import path
from App import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
]