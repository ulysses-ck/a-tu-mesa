from django.urls import path
from . import views

urlpatterns = [
    path('ticket', views.FacturaView.as_view(), name='ticket'),
]