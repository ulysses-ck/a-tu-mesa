from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Mesa
from common.mixins import LoginRequidMixinWithLoginURL


class MesaView(TemplateView):
    name = "mesa"
    template_name = "mesa.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mesas"] = Mesa.objects.all()
        return context


class CreateMesaView(LoginRequidMixinWithLoginURL, CreateView):
    model = Mesa
    fields = [
        "nro_mesa",
    ]
    template_name = "mesa_create.html"
    success_url = "/mesa"


class UpdateMesaView(LoginRequidMixinWithLoginURL, UpdateView):
    model = Mesa
    fields = [
        "nro_mesa",
    ]
    template_name = "mesa_update.html"
    success_url = "/mesa"


class DeleteMesaView(LoginRequidMixinWithLoginURL, DeleteView):
    model = Mesa
    template_name = "mesa_delete.html"
    success_url = "/mesa"
