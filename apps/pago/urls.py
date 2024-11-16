from django.urls import path
from . import views

urlpatterns = [
    path('pago', views.PagoView.as_view(), name='pago'),
]