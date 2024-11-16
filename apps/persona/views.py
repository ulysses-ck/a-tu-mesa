from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Persona

class PersonaView(TemplateView):
    name = 'persona'
    template_name = 'persona.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personas'] = Persona.objects.all()
        return context

class CreatePersonaView(CreateView):
    model = Persona
    fields = [
        'user',
        'nombre',
        'apellido',
        'rol',
        'correo',
        'telefono',
        'documento',
    ]
    template_name = 'persona_create.html'
    success_url = '/persona'

class UpdatePersonaView(UpdateView):
    model = Persona
    fields = [
        'user',
        'nombre',
        'apellido',
        'rol',
        'correo',
        'telefono',
        'documento',
    ]
    template_name = 'persona_update.html'
    success_url = '/persona'

class DeletePersonaView(DeleteView):
    model = Persona
    template_name = 'persona_delete.html'
    success_url = '/persona'   

