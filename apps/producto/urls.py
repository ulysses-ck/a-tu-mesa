from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.ProductoView.as_view(), name='producto'),
]