from django.views.generic import TemplateView
from .models import Home

class HomeView(TemplateView):
	name = 'home'

	urls = Home.objects.all()
	template_name = 'home.html'

	# render name in template
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['name'] = self.name
		context['urls'] = self.urls
		return context