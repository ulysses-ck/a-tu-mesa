from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView
from .models import Mesa
from apps.comanda.models import Comanda
from common.mixins import LoginRequidMixinWithLoginURL
from .forms import TicketForm
from django.contrib import messages


class MesaView(TemplateView):
    name = "mesa"
    template_name = "mesa.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mesas = Mesa.objects.all()
        mesas_estado = []
        
        for mesa in mesas:
            comandas = Comanda.objects.filter(mesa=mesa)
            
            """recorro las mesas revisando si tienen comandas, si las tienen y estan para entregar,
            si las tienen y estan en preparacion o si simplemente estan ocupadas"""
            if not comandas.exists():
                estado = "Libre"
            elif comandas.filter(estado__nombre="Para Entregar").exists():
                estado = "Para Entregar"
            elif comandas.filter(estado__nombre="En Preparación").exists():
                estado = "En Preparacion"
            else:
                estado = "Ocupada"
            
            "Cualquiera sea el resultado, esto se agrega a la lista de mesas a iterar"
            
            mesas_estado.append({
                "mesa": mesa,
                "estado": estado
            })
            context["mesas_estado"] = mesas_estado
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

class CajaView(FormView):
    name = "caja"
    template_name = "caja.html"
    form_class = TicketForm


    def get_context_data(self, **kwargs):
        mesa_seleccionada = self.request.GET.get("mesa")
        if mesa_seleccionada:
            context = super().get_context_data(**kwargs)
            context["mesas"] = Mesa.objects.all()
            context['comandas'] = Comanda.objects.filter(mesa__nro_mesa=mesa_seleccionada)
            context['valor_total'] = sum([comanda.producto.precio for comanda in context['comandas']])
            context['ticket_form'] = TicketForm()
            

            return context
        context = super().get_context_data(**kwargs)
        context["mesas"] = Mesa.objects.all()
        return context
    
    def form_valid(self, form):
        ticket_form = TicketForm(self.request.POST)

        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.save()
            messages.success(self.request, "Ticket creado con éxito.")
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Error al crear el ticket')
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el ticket')
        return self.render_to_response(self.get_context_data(form=form))