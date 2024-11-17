from django.urls import path
from . import views

urlpatterns = [
    path('tipoDePedido', views.TipoDePedidoView.as_view(), name='tipoDePedido'),
    path('tipoDePedido/create/', views.CreateTipoDePedidoView.as_view(), name='create_tipoDePedido'),
    path('tipoDePedido/update/<int:pk>/', views.UpdateTipoDePedidoView.as_view(), name='update_tipoDePedido'),
    path('tipoDePedido/delete/<int:pk>/', views.DeleteTipoDePedidoView.as_view(), name='delete_tipoDePedido'),
]