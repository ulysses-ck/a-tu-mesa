from django.urls import path
from . import views

urlpatterns = [
    path('facturas', views.FacturaView.as_view(), name='facturas'),
]