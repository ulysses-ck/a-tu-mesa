from django.urls import path
from . import views

urlpatterns = [
    path('comandas', views.ComandasView.as_view(), name='home'),
]