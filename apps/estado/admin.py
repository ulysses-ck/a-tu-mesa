from django.contrib import admin

# Register your models here.
from apps.estado.models import Estado

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
