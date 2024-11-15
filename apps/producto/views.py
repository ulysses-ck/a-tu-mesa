from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Producto
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

class ProductoView(TemplateView):
    name = 'producto'
    template_name = 'producto.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context