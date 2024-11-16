from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Rol
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

class RolView(TemplateView):
    name = 'Rol'
    template_name = 'Rol.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Rol'] = Rol.objects.all()
        return context
