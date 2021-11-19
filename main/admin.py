from django.contrib import admin
from .models import Exhibition
from .models import Tickets


class PostAdmin(admin.ModelAdmin):
    list_display = ('name_of_exh', 'places')
    readonly_fields = ('sold_tickets',)


class PostAdminTickets(admin.ModelAdmin):
    list_display = ('name', 'buyer', 'number_of_ticket')


admin.site.register(Exhibition, PostAdmin)
admin.site.register(Tickets, PostAdminTickets)
