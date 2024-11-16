from django.urls import path
from . import views

urlpatterns = [
    path('rol', views.RolView.as_view(), name='rol'),
]