from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.HomeAbout.as_view(), name='about'),
    path('edit/', views.HomeEditView.as_view(), name='edit_home'),
    path('login/', views.LoginView.as_view(), name='login'),
] 