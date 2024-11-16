from django.urls import path
from . import views

urlpatterns = [
    path('facturas', views.FacturaView.as_view(), name='facturas'),
    path('factura/create/', views.CreateFacturaView.as_view(), name='create_factura'),
    path('factura/update/<int:pk>/', views.UpdateFacturaView.as_view(), name='update_factura'),
    path('factura/delete/<int:pk>/', views.DeleteFacturaView.as_view(), name='delete_factura'),
]