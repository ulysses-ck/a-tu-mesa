from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Pago
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

class PagoView(TemplateView):
    name = 'Pago'
    template_name = 'pago.html'
    
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
