from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from .models import Comanda
from apps.estado.models import Estado
from common.mixins import LoginRequidMixinWithLoginURL
from django.utils import timezone
from django.contrib import messages

class ComandasView(LoginRequidMixinWithLoginURL ,TemplateView):
    name = 'comanda'
    template_name = 'comanda_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comandas'] = Comanda.objects.all()
        return context

class CreateComandaView(LoginRequidMixinWithLoginURL, CreateView):
    model = Comanda
    fields = [
        'producto',
        'cantidad',
        'estado',
        'tipo_de_pedido',
        'ticket',
        'mesa',
        'fecha'
    ]
    template_name = 'comanda_create.html'
    success_url = '/comanda'
    
    def get_initial(self):
        initial = super().get_initial()
        initial['fecha'] = timezone.now()
        return initial

class UpdateComandaView(LoginRequidMixinWithLoginURL, UpdateView):
    model = Comanda
    fields = [
        'producto',
        'cantidad',
        'estado',
        'tipo_de_pedido',
        'ticket',
        'mesa',
        'fecha'
    ]
    template_name = 'comanda_update.html'
    success_url = '/comanda'

class DeleteComandaView(LoginRequidMixinWithLoginURL, DeleteView):
    model = Comanda
    template_name = 'comanda_delete.html'
    success_url = '/comanda'

class CocinaView(TemplateView):
    template_name = 'cocina.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comandas'] = Comanda.objects.all()
        context['estados'] = Estado.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        comanda_id = request.POST.get('comanda_id')
        nuevo_estado_id = request.POST.get('estado_id')
        
        if not comanda_id or not nuevo_estado_id:
            messages.error(request, 'Datos incompletos para actualizar el estado')
            return redirect('cocina')
        
        try:
            comanda = Comanda.objects.get(id=comanda_id)
            estado = Estado.objects.get(id=nuevo_estado_id)
            
            comanda.estado = estado
            comanda.save()
            messages.success(request, f'Estado de comanda #{comanda_id} actualizado a {estado.nombre}')
            
        except Comanda.DoesNotExist:
            messages.error(request, f'No se encontró la comanda #{comanda_id}')
        except Estado.DoesNotExist:
            messages.error(request, f'Estado inválido')
        except Exception as e:
            messages.error(request, f'Error al actualizar el estado: {str(e)}')
            
        return redirect('cocina')
