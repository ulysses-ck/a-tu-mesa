from django.urls import path
from . import views

urlpatterns = [
    path('usuario', views.UsuarioView.as_view(), name='usuario'),
]