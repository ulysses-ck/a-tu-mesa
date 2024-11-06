from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Home
from django.contrib import messages

class HomeView(TemplateView):
	name = 'home'
	template_name = 'home.html'

	# render name in template
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		home_instance = Home.objects.first()
		context['banner'] = home_instance.banner
		context['botonmenu'] = home_instance.botonMenu
		context['botonreservacion'] = home_instance.botonReservation
		context['botonseguimientodepedido'] = home_instance.botonSeguimientoDePedido

		return context


class HomeEditView(TemplateView):
    name = 'edit_home'
    template_name = 'home_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home = Home.objects.first()
        context['banner'] = home.banner
        context['botonmenu'] = home.botonMenu
        context['botonreservacion'] = home.botonReservation
        context['botonseguimientodepedido'] = home.botonSeguimientoDePedido
        return context

    def post(self, request, *args, **kwargs):
        home = Home.objects.first()
        context = self.get_context_data(**kwargs)

        if not home:
            home = Home.objects.create()

        if request.method == 'POST':
            home.banner = request.POST.get('banner', '')
            home.botonmenu = request.POST.get('botonmenu', '')
            home.botonreservacion = request.POST.get('botonreservacion', '')
            home.botonseguimientodepedido = request.POST.get('botonseguimientodepedido', '')
            
        home.save()
        messages.success(request, 'Contenido actualizado exitosamente')
        return redirect('edit_home')

