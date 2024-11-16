from django.urls import path
from . import views

urlpatterns = [
    path('persona', views.PersonaView.as_view(), name='persona'),
]