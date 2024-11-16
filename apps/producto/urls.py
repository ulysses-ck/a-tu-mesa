from django.urls import path
from . import views

urlpatterns = [
    path('producto', views.ProductoView.as_view(), name='producto'),
]