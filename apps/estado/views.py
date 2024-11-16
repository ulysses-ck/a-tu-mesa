from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Estado
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

class ComandaView(TemplateView):
    name = 'estado'
    template_name = 'estado.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estado'] = Estado.objects.all()
        return context

# Create your views here.
