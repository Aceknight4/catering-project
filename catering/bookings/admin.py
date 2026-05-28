from django.contrib import admin
from django.contrib import admin
from .models import Booking, Message

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display  = ['name', 'event_type', 
                     'event_date', 'status', 
                     'created_at']
    list_filter   = ['status', 'event_type']
    search_fields = ['name', 'email']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display  = ['name', 'email', 'created_at']
    search_fields = ['name', 'email']


