from django.urls import path
from . import views

urlpatterns = [
    path('estado', views.EstadoView.as_view(), name='estado'),
    path('estado/create/', views.CreateEstadoView.as_view(), name='create_estado'),
    path('estado/update/<int:pk>/', views.UpdateEstadoView.as_view(), name='update_estado'),
    path('estado/delete/<int:pk>/', views.DeleteEstadoView.as_view(), name='delete_estado'),
]