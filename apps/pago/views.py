from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Pago, FormaDePago
from common.mixins import LoginRequidMixinWithLoginURL


# pago
class PagoView(LoginRequidMixinWithLoginURL, TemplateView):
    name = "Pago"
    template_name = "pago_read.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pagos"] = Pago.objects.all()
        return context


class CreatePagoView(LoginRequidMixinWithLoginURL, CreateView):
    model = Pago
    fields = [
        "nro_autorizacion",
        "fecha",
        "pagador",
        "forma_de_pago",
    ]
    template_name = "pago_create.html"
    success_url = "/pago"


class UpdatePagoView(LoginRequidMixinWithLoginURL, UpdateView):
    model = Pago
    fields = [
        "nro_autorizacion",
        "fecha",
        "pagador",
        "forma_de_pago",
    ]
    template_name = "pago_update.html"
    success_url = "/pago"


class DeletePagoView(LoginRequidMixinWithLoginURL, DeleteView):
    model = Pago
    template_name = "pago_delete.html"
    success_url = "/pago"


# forma pago


class FormaPagoView(LoginRequidMixinWithLoginURL, TemplateView):
    template_name = "formapago_read.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formas_pagos"] = FormaDePago.objects.all()
        return context


class CreateFormaPagoView(LoginRequidMixinWithLoginURL, CreateView):
    model = FormaDePago
    fields = [
        "nombre",
    ]
    template_name = "formapago_create.html"
    success_url = "/forma_pago"


class UpdateFormaPagoView(LoginRequidMixinWithLoginURL, UpdateView):
    model = FormaDePago
    fields = [
        "nombre",
    ]
    template_name = "formapago_update.html"
    success_url = "/forma_pago"


class DeleteFormaPagoView(LoginRequidMixinWithLoginURL, DeleteView):
    model = FormaDePago
    template_name = "formapago_delete.html"
    success_url = "/forma_pago"
