from django.views.generic import TemplateView
from .models import Home

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