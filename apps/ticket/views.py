from django.views.generic import TemplateView
from .models import Ticket

class TicketView(TemplateView):
    name = 'Ticket'
    template_name = 'ticket_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Ticket'] = Ticket.objects.all()
        return context
