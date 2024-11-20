from django.apps import AppConfig


class EstadoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.estado'
    
    def ready(self):
        from . import signals
