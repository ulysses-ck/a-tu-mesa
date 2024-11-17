from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Pago, FormaDePago

# pago
class PagoView(TemplateView):
    name = 'Pago'
    template_name = 'pago_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagos'] = Pago.objects.all()
        return context
class CreatePagoView(CreateView):
    model = Pago
    fields = [
        'nro_autorizacion',
        'fecha',
        'pagador',
        'forma_de_pago',
    ]
    template_name = 'pago_create.html'
    success_url = '/pago'

class UpdatePagoView(UpdateView):
    model = Pago
    fields = [
        'nro_autorizacion',
        'fecha',
        'pagador',
        'forma_de_pago',
    ]
    template_name = 'pago_update.html'
    success_url = '/pago'

class DeletePagoView(DeleteView):
    model = Pago
    template_name = 'pago_delete.html'
    success_url = '/pago'   


# forma pago

class FormaPagoView(TemplateView):
    template_name = 'formapago_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formas_pagos'] = FormaDePago.objects.all()
        return context
    
class CreateFormaPagoView(CreateView):
    model = FormaDePago
    fields = [
        'nombre',
    ]
    template_name = 'formapago_create.html'
    success_url = '/forma_pago'

class UpdateFormaPagoView(UpdateView):
    model = FormaDePago
    fields = [
        'nombre',
    ]
    template_name = 'formapago_update.html'
    success_url = '/forma_pago'

class DeleteFormaPagoView(DeleteView):
    model = FormaDePago
    template_name = 'formapago_delete.html'
    success_url = '/forma_pago'