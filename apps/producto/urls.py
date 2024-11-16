from django.urls import path
from . import views

urlpatterns = [
    # esto es para el menu vista cliente
    path('menu', views.ProductoView.as_view(), name='producto'),

    # admin
    path('producto/', views.ProductoAdminView.as_view(), name='producto_admin'),
    path('producto/create/', views.CreateProductoView.as_view(), name='create_producto'),
    path('producto/update/<int:pk>/', views.UpdateProductoView.as_view(), name='update_producto'),
    path('producto/delete/<int:pk>/', views.DeleteProductoView.as_view(), name='delete_producto'),
]