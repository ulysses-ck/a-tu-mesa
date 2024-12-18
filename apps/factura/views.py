from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Factura
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from common.mixins import LoginRequidMixinWithLoginURL


# Create your views here.
@method_decorator(login_required, name="dispatch")
class FacturaView(LoginRequidMixinWithLoginURL, TemplateView):
    name = "facturas"
    template_name = "facturas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["facturas"] = Factura.objects.all()
        return context


class CreateFacturaView(LoginRequidMixinWithLoginURL, CreateView):
    model = Factura
    fields = [
        "pago",
        "ticket",
    ]
    template_name = "factura_create.html"
    success_url = "/factura"


class UpdateFacturaView(LoginRequidMixinWithLoginURL, UpdateView):
    model = Factura
    fields = [
        "pago",
        "ticket",
    ]
    template_name = "factura_update.html"
    success_url = "/factura"


class DeleteFacturaView(LoginRequidMixinWithLoginURL, DeleteView):
    model = Factura
    template_name = "factura_delete.html"
    success_url = "/factura"
