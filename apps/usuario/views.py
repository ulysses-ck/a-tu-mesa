from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Usuario
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator
from common.mixins import LoginRequidMixinWithLoginURL


class UsuarioView(LoginRequidMixinWithLoginURL, TemplateView):
    name = "Usuario"
    template_name = "usuario_read.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Usuario"] = Usuario.objects.all()
        return context
