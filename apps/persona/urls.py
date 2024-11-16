from django.urls import path
from . import views

urlpatterns = [
    path('persona', views.PersonaView.as_view(), name='persona'),
    path('persona/create/', views.CreatePersonaView.as_view(), name='create_persona'),
    path('persona/update/<int:pk>/', views.UpdatePersonaView.as_view(), name='update_persona'),
    path('persona/delete/<int:pk>/', views.DeletePersonaView.as_view(), name='delete_persona'),
]