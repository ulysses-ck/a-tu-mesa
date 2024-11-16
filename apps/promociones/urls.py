from django.urls import path
from . import views

urlpatterns = [
    path('promociones', views.PromocionesView.as_view(), name='promociones'),
]