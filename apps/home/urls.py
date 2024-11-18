from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.HomeAbout.as_view(), name='about'),
    path('edit/', views.HomeEditView.as_view(), name='edit_home'),
    path('create/', views.UserCreateForm.as_view(), name='user_create'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
] 