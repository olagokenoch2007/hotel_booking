from django.contrib import admin

# Register your models here.

from .models import *

## page ,filter  and search
@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at', 'updated_at']
    list_editable = ['price']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 5

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']

admin.site.register(Staff)

admin.site.register(Booking)