from django.views.generic import TemplateView
from .models import Rol

class RolView(TemplateView):
    name = 'Rol'
    template_name = 'rol_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Rol'] = Rol.objects.all()
        return context
