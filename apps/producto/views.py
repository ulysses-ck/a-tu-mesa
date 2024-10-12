from django.views.generic import TemplateView
from .models import Producto

class HomeView(TemplateView):
	name = 'home'
	
	# get all productos from database
	productos = Producto.objects.all()
	template_name = 'index.html'
	
	# render name in template
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['name'] = self.name
		context['productos'] = self.productos
		return context