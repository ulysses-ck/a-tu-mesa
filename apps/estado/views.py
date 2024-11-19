from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Estado
from common.mixins import LoginRequidMixinWithLoginURL


class EstadoView(LoginRequidMixinWithLoginURL, TemplateView):
    name = "estado"
    template_name = "estado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estados"] = Estado.objects.all()
        return context


class CreateEstadoView(LoginRequidMixinWithLoginURL, CreateView):
    model = Estado
    fields = [
        "nombre",
    ]
    template_name = "estado_create.html"
    success_url = "/estado"


class UpdateEstadoView(LoginRequidMixinWithLoginURL, UpdateView):
    model = Estado
    fields = [
        "nombre",
    ]
    template_name = "estado_update.html"
    success_url = "/estado"


class DeleteEstadoView(LoginRequidMixinWithLoginURL, DeleteView):
    model = Estado
    template_name = "estado_delete.html"
    success_url = "/estado"
