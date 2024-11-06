from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Home
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

@method_decorator(xframe_options_exempt, name='dispatch')
class HomeView(TemplateView):
	name = 'home'
	template_name = 'home.html'

	# render name in template
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		home_instance = Home.objects.first()
		if home_instance:
			context['banner'] = home_instance.banner
			context['botonmenu'] = home_instance.botonMenu
			context['botonreservacion'] = home_instance.botonReservation
			context['botonseguimientodepedido'] = home_instance.botonSeguimientoDePedido
		return context

@method_decorator(xframe_options_exempt, name='dispatch')
class HomeEditView(TemplateView):
    name = 'edit_home'
    template_name = 'home_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home = Home.objects.first()
        if home:
            context['banner'] = home.banner
            context['botonmenu'] = home.botonMenu
            context['botonreservacion'] = home.botonReservation
            context['botonseguimientodepedido'] = home.botonSeguimientoDePedido
        return context

    def post(self, request, *args, **kwargs):
        home = Home.objects.first()
        if not home:
            home = Home.objects.create()

        # Actualizar usando los nombres correctos del modelo
        home.banner = request.POST.get('banner', '')
        home.botonMenu = request.POST.get('botonmenu', '')  # Notar la M mayúscula
        home.botonReservation = request.POST.get('botonreservacion', '')  # Notar la R mayúscula
        home.botonSeguimientoDePedido = request.POST.get('botonseguimientodepedido', '')  # Notar las mayúsculas
        
        home.save()
        messages.success(request, 'Contenido actualizado exitosamente')
        return self.render_to_response(self.get_context_data(**kwargs))

