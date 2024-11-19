from .models import TipoProducto
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from common.mixins import LoginRequidMixinWithLoginURL


class TipoProductoView(LoginRequidMixinWithLoginURL, TemplateView):
    name = "TipoProducto"
    template_name = "tipo_producto_read.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipoProductos"] = TipoProducto.objects.all()
        return context


class CreateTipoProductoView(LoginRequidMixinWithLoginURL, CreateView):
    model = TipoProducto
    fields = ["nombre"]
    template_name = "tipo_producto_create.html"
    success_url = "/tipoProducto"


class UpdateTipoProductoView(LoginRequidMixinWithLoginURL, UpdateView):
    model = TipoProducto
    fields = ["nombre"]
    template_name = "tipo_producto_update.html"
    success_url = "/tipoProducto"


class DeleteTipoProductoView(LoginRequidMixinWithLoginURL, DeleteView):
    model = TipoProducto
    template_name = "tipo_producto_delete.html"
    success_url = "/tipoProducto"
