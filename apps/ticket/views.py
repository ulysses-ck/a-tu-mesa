from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Ticket
from common.mixins import LoginRequidMixinWithLoginURL
from django.utils import timezone


class TicketView(LoginRequidMixinWithLoginURL, TemplateView):
    name = "Ticket"
    template_name = "ticket_read.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.all()
        return context


class CreateTicketView(LoginRequidMixinWithLoginURL, CreateView):
    model = Ticket
    fields = [
        "promocion",
        "fecha",
        "notas",
    ]
    template_name = "ticket_create.html"
    success_url = "/ticket"
    def get_initial(self):
        initial = super().get_initial()
        initial['fecha'] = timezone.now()
        return initial


class UpdateTicketView(LoginRequidMixinWithLoginURL, UpdateView):
    model = Ticket
    fields = [
        "promocion",
        "fecha",
        "notas",
    ]
    template_name = "ticket_update.html"
    success_url = "/ticket"


class DeleteTicketView(LoginRequidMixinWithLoginURL, DeleteView):
    model = Ticket
    template_name = "ticket_delete.html"
    success_url = "/ticket"
