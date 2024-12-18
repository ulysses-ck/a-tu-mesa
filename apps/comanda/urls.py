from django.urls import path
from . import views

urlpatterns = [
    path('comanda/', views.ComandasView.as_view(), name='comanda'),
    path('comanda/create/', views.CreateComandaView.as_view(), name='create_comanda'),
    path('comanda/update/<int:pk>/', views.UpdateComandaView.as_view(), name='update_comanda'),
    path('comanda/delete/<int:pk>/', views.DeleteComandaView.as_view(), name='delete_comanda'),

    path('cocina/', views.CocinaView.as_view(), name='cocina'),
]