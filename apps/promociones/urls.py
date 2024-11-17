from django.urls import path
from . import views

urlpatterns = [
    path('promociones', views.PromocionesView.as_view(), name='promociones'),
    path('promociones/create/', views.CreatePromocionesView.as_view(), name='create_promociones'),
    path('promociones/update/<int:pk>/', views.UpdatePromocionesView.as_view(), name='update_promociones'),
    path('promociones/delete/<int:pk>/', views.DeletePromocionesView.as_view(), name='delete_promociones'),
]