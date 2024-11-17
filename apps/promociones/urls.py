from django.urls import path
from . import views

urlpatterns = [
    # promociones
    path('promociones', views.PromocionesView.as_view(), name='promociones'),
    path('promociones/create/', views.CreatePromocionesView.as_view(), name='create_promociones'),
    path('promociones/update/<int:pk>/', views.UpdatePromocionesView.as_view(), name='update_promociones'),
    path('promociones/delete/<int:pk>/', views.DeletePromocionesView.as_view(), name='delete_promociones'),

    # condiciones
    path('condiciones', views.CondicionesView.as_view(), name='condiciones'),
    path('condiciones/create/', views.CreateCondicionesView.as_view(), name='create_condiciones'),
    path('condiciones/update/<int:pk>/', views.UpdateCondicionesView.as_view(), name='update_condiciones'),
    path('condiciones/delete/<int:pk>/', views.DeleteCondicionesView.as_view(), name='delete_condiciones'),
]