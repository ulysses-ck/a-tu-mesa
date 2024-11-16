from django.urls import path
from . import views

urlpatterns = [
    path('mesa', views.MesaView.as_view(), name='mesa'),
]