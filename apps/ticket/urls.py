from django.urls import path
from . import views

urlpatterns = [
    path('ticket', views.TicketView.as_view(), name='ticket'),
    path('ticket/create/', views.CreateTicketView.as_view(), name='create_ticket'),
    path('ticket/update/<int:pk>/', views.UpdateTicketView.as_view(), name='update_ticket'),    
    path('ticket/delete/<int:pk>/', views.DeleteTicketView.as_view(), name='delete_ticket'),
]