"""
URL configuration for atumesa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('', include('apps.producto.urls')),
    path('', include('apps.factura.urls')),
    path('', include('apps.comanda.urls')),
    path('', include('apps.estado.urls')),
    path('', include('apps.mesa.urls')),
    path('', include('apps.pago.urls')), 
    path('', include('apps.persona.urls')),
    path('', include('apps.promociones.urls')),
    path('', include('apps.rol.urls')),
    path('', include('apps.ticket.urls')),
    path('', include('apps.usuario.urls')),
    path('', include('apps.tipoProducto.urls')),
    path('administracion/', TemplateView.as_view(template_name='administracion.html'), name='administracion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
