from django.urls import path
from . import views

urlpatterns = [
    path('pago', views.PagoView.as_view(), name='pago'),
    path('pago/create/', views.CreatePagoView.as_view(), name='create_pago'),
    path('pago/update/<int:pk>/', views.UpdatePagoView.as_view(), name='update_pago'),
    path('pago/delete/<int:pk>/', views.DeletePagoView.as_view(), name='delete_pago'),
]