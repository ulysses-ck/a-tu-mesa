from django.urls import path
from . import views

urlpatterns = [
    path('ticket', views.TicketView.as_view(), name='ticket'),
]