from django.contrib import admin

# Register your models here.
from apps.mesa.models import Mesa

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
	list_display = ('nro_mesa',)
