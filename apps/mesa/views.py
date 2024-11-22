from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView
from .models import Mesa
from apps.ticket.models import Ticket
from apps.comanda.models import Comanda
from apps.producto.models import Producto
from common.mixins import LoginRequidMixinWithLoginURL
from .forms import TicketForm, ComandaForm
from django.contrib import messages
from django.utils import timezone, dateformat
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse


def rev_comanda_estado(mesa):
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
    return estado

class MesaView(TemplateView):
    name = "mesa"
    template_name = "mesa.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mesas = Mesa.objects.all()
        mesas_estado = []
        for mesa in mesas:
            estado = rev_comanda_estado(mesa)
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

class CajaView(TemplateView):
    template_name = "caja.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mesa_seleccionada = self.request.GET.get("mesa")
        context = super().get_context_data(**kwargs)
        mesas = Mesa.objects.all()
        mesas_estado = []
        for mesa in mesas:
            estado = rev_comanda_estado(mesa)
            "Cualquiera sea el resultado, esto se agrega a la lista de mesas a iterar"
            mesas_estado.append({
                "mesa": mesa,
                "estado": estado
            })
        context["mesas_estado"] = mesas_estado
        context["mesas"] = Mesa.objects.all()
        if mesa_seleccionada:
            context["productos"] = Producto.objects.all()
            context['fecha'] = dateformat.format(timezone.now(), 'd/m/Y')
            context['comandas'] = Comanda.objects.filter(mesa__nro_mesa=mesa_seleccionada)
            context['valor_total'] = sum([comanda.producto.precio for comanda in context['comandas']])
            context['ticket_form'] = TicketForm()
            context['mesa_seleccionada'] = Mesa.objects.get(nro_mesa=mesa_seleccionada)
        return context

    def post(self, request, *args, **kwargs):
        if 'crear_comanda' in request.POST:
            comanda_form = ComandaForm(request.POST)
            if comanda_form.is_valid():
                comanda = comanda_form.save(commit=False)
                comanda.save()
                messages.success(request, "Comanda creada exitosamente")
                return redirect(f"{reverse('caja')}?mesa={request.POST.get('mesa')}")
            else:
                messages.error(request, "Error al crear comanda")
                return self.render_to_response(self.get_context_data(comanda_form=comanda_form))

        elif 'crear_ticket' in request.POST:
            ticket_form = TicketForm(request.POST)
            if ticket_form.is_valid():
                ticket = ticket_form.save(commit=False)
                ticket.save()
                messages.success(request, "Ticket creado exitosamente")
                return redirect('caja')
            else:
                messages.error(request, "Error en el formulario del ticket")
                return self.render_to_response(self.get_context_data(ticket_form=ticket_form))

        return self.render_to_response(self.get_context_data())

