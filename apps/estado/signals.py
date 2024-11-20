from django.db.models.signals import post_migrate
from django.dispatch import receiver
from apps.estado.models import Estado

@receiver(post_migrate)
def crear_estados_iniciales(sender, **kwargs):
    
    if sender.name == "apps.estado":
        estados_iniciales = ["En Preparación", "Para Entregar", "Terminado", "Terminado"]
        for estado_name in estados_iniciales:
            Estado.objects.get_or_create(nombre=estado_name)