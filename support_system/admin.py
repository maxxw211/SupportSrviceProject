from django.contrib import admin

from .models import SupportResponse, Ticket


class SupportAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'created_at', 'ticket')
    list_display_links = ('id', 'answer')
    search_fields = ('answer', 'ticket')
    list_filter = ('ticket', 'answer', 'created_at')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at', 'updated_at', 'status_ticket')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('status_ticket',)
    list_filter = ('status_ticket', 'user')


admin.site.register(SupportResponse, SupportAnswerAdmin)
admin.site.register(Ticket, TicketAdmin)
