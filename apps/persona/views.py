from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Persona
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

class ComandaView(TemplateView):
    name = 'persona'
    template_name = 'persona.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persona'] = Persona.objects.all()
        return context