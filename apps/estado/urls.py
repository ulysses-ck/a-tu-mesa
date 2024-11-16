from django.urls import path
from . import views

urlpatterns = [
    path('estado', views.EstadoView.as_view(), name='estado'),
]