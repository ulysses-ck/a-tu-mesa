from django.contrib import admin
from apps.ticket.models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'notas')
