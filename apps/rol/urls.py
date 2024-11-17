from django.urls import path
from . import views

urlpatterns = [
    path('rol', views.RolView.as_view(), name='rol'),
    path('rol/create/', views.CreateRolView.as_view(), name='create_rol'),
    path('rol/update/<int:pk>/', views.UpdateRolView.as_view(), name='update_rol'),
    path('rol/delete/<int:pk>/', views.DeleteRolView.as_view(), name='delete_rol'),
]