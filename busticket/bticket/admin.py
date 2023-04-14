from django.contrib import admin
from bticket.models import Ticket
class TicketAdmin(admin.ModelAdmin):
    list_display=['full_name','date','id','From','To','price']
admin.site.register(Ticket,TicketAdmin)
