from django.urls import path
from . import views

urlpatterns = [
    path('estado', views.FacturaView.as_view(), name='estado'),
]