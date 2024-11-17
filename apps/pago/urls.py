from django.urls import path
from . import views

urlpatterns = [
    # pago
    path('pago', views.PagoView.as_view(), name='pago'),
    path('pago/create/', views.CreatePagoView.as_view(), name='create_pago'),
    path('pago/update/<int:pk>/', views.UpdatePagoView.as_view(), name='update_pago'),
    path('pago/delete/<int:pk>/', views.DeletePagoView.as_view(), name='delete_pago'),

    # forma pago
    path('forma_pago', views.FormaPagoView.as_view(), name='forma_pago'),
    path('forma_pago/create/', views.CreateFormaPagoView.as_view(), name='create_forma_pago'),
    path('forma_pago/update/<int:pk>/', views.UpdateFormaPagoView.as_view(), name='update_forma_pago'),
    path('forma_pago/delete/<int:pk>/', views.DeleteFormaPagoView.as_view(), name='delete_forma_pago'),
]