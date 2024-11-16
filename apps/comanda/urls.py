from django.urls import path
from . import views

urlpatterns = [
    path('comandas', views.ComandasView.as_view(), name='home'),
    path('comandas/create/', views.CreateComandaView.as_view(), name='create_comanda'),
    path('comandas/update/<int:pk>/', views.UpdateComandaView.as_view(), name='update_comanda'),
    path('comandas/delete/<int:pk>/', views.DeleteComandaView.as_view(), name='delete_comanda'),
]