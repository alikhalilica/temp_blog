from django.contrib import admin
from .models import ContactTickets
# Register your models here.
class ContactTicketAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message']
    
admin.site.register(ContactTickets,ContactTicketAdmin)