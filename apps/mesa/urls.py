from django.urls import path
from . import views

urlpatterns = [
    path('mesa', views.MesaView.as_view(), name='mesa'),
    path('mesa/create/', views.CreateMesaView.as_view(), name='create_mesa'),
    path('mesa/update/<int:pk>/', views.UpdateMesaView.as_view(), name='update_mesa'),
    path('mesa/delete/<int:pk>/', views.DeleteMesaView.as_view(), name='delete_mesa'),
]