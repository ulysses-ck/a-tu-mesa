from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Rol

class RolView(TemplateView):
    name = 'Rol'
    template_name = 'rol_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rols'] = Rol.objects.all()
        return context

class CreateRolView(CreateView):
    model = Rol
    fields = ['nombre']
    template_name = 'rol_create.html'
    success_url = '/rol'

class UpdateRolView(UpdateView):
    model = Rol
    fields = ['nombre']
    template_name = 'rol_update.html'
    success_url = '/rol'

class DeleteRolView(DeleteView):
    model = Rol
    template_name = 'rol_delete.html'
    success_url = '/rol'