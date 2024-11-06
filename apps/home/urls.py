from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('edit/', views.HomeEditView.as_view(), name='edit_home'),
] 