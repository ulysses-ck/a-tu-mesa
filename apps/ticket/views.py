from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Ticket

class TicketView(TemplateView):
    name = 'Ticket'
    template_name = 'ticket_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.all()
        return context

class CreateTicketView(CreateView):
    model = Ticket
    fields = [
        'promocion',
        'fecha',
        'notas',
    ]
    template_name = 'ticket_create.html'
    success_url = '/ticket'

class UpdateTicketView(UpdateView):
    model = Ticket
    fields = [
        'promocion',
        'fecha',
        'notas',
    ]
    template_name = 'ticket_update.html'
    success_url = '/ticket'

class DeleteTicketView(DeleteView):
    model = Ticket
    template_name = 'ticket_delete.html'
    success_url = '/ticket'   
