# setup urls
from django.urls import path
from . import views

urlpatterns = [
    path('tipoProducto', views.TipoProductoView.as_view(), name='tipoProducto'),
    path('tipoProducto/create/', views.CreateTipoProductoView.as_view(), name='create_tipoProducto'),
    path('tipoProducto/update/<int:pk>/', views.UpdateTipoProductoView.as_view(), name='update_tipoProducto'),
    path('tipoProducto/delete/<int:pk>/', views.DeleteTipoProductoView.as_view(), name='delete_tipoProducto'),
]