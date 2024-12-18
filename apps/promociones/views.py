from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Promociones, Condiciones
from django.utils import timezone

from common.mixins import LoginRequidMixinWithLoginURL


# promociones
class PromocionesView(LoginRequidMixinWithLoginURL, TemplateView):
    name = "promociones"
    template_name = "promociones.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["promociones"] = Promociones.objects.all()
        return context


class CreatePromocionesView(CreateView):
    model = Promociones
    fields = [
        "descuento",
        "descripcion",
        "condiciones",
    ]
    template_name = "promociones_create.html"
    success_url = "/promociones"


class UpdatePromocionesView(UpdateView):
    model = Promociones
    fields = [
        "descuento",
        "descripcion",
        "condiciones",
    ]
    template_name = "promociones_update.html"
    success_url = "/promociones"


class DeletePromocionesView(DeleteView):
    model = Promociones
    template_name = "promociones_delete.html"
    success_url = "/promociones"


# condiciones


class CondicionesView(TemplateView):
    name = "condiciones"
    template_name = "condiciones_read.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["condiciones_list"] = Condiciones.objects.all()
        return context


class CreateCondicionesView(CreateView):
    model = Condiciones
    fields = [
        "inicio",
        "expira",
        "producto",
    ]
    template_name = "condiciones_create.html"
    success_url = "/condiciones"
    
    def get_initial(self):
        initial = super().get_initial()
        initial['inicio'] = timezone.now()
        return initial


class UpdateCondicionesView(UpdateView):
    model = Condiciones
    fields = [
        "inicio",
        "expira",
        "producto",
    ]
    template_name = "condiciones_update.html"
    success_url = "/condiciones"


class DeleteCondicionesView(DeleteView):
    model = Condiciones
    template_name = "condiciones_delete.html"
    success_url = "/condiciones"
