from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Mesa
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

class ComandaView(TemplateView):
    name = 'mesa'
    template_name = 'mesa.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mesa'] = Mesa.objects.all()
        return context
