from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Producto
from apps.tipoProducto.models import TipoProducto
from common.mixins import LoginRequidMixinWithLoginURL


class ProductoView(TemplateView):
    name = "producto"
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los tipos seleccionados desde los parámetros de la URL
        tipos_seleccionados = self.request.GET.getlist("tipo")

        # Filtrar los productos según los tipos seleccionados
        if tipos_seleccionados:
            context["productos"] = Producto.objects.filter(
                tipo__nombre__in=tipos_seleccionados
            )
        else:
            context["productos"] = Producto.objects.all()

        # Obtener todos los tipos de productos para el formulario de filtro
        context["tipos"] = TipoProducto.objects.all()
        context["tipos_seleccionados"] = tipos_seleccionados

        return context


class ProductoAdminView(LoginRequidMixinWithLoginURL, TemplateView):
    name = "producto_admin"
    template_name = "producto_read.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos"] = Producto.objects.all()
        return context


class CreateProductoView(LoginRequidMixinWithLoginURL, CreateView):
    model = Producto
    fields = [
        "precio",
        "nombre",
        "tipo",
        "imagen",
    ]
    template_name = "producto_create.html"
    success_url = "/producto"


class UpdateProductoView(LoginRequidMixinWithLoginURL, UpdateView):
    model = Producto
    fields = [
        "precio",
        "nombre",
        "tipo",
        "imagen",
    ]
    template_name = "producto_update.html"
    success_url = "/producto"


class DeleteProductoView(LoginRequidMixinWithLoginURL, DeleteView):
    model = Producto
    template_name = "producto_delete.html"
    success_url = "/producto"
