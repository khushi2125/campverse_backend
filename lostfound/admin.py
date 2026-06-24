# Admin configuration for the lost and found application, registering the LostFoundItem model with the Django admin interface to allow for easy management of lost and found items. The admin class includes customizations for list display, filtering, searching, and ordering of lost and found items in the admin panel.
from django.contrib import admin
from .models import LostFoundItem
@admin.register(LostFoundItem)
class LostFoundItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'location', 'date', 'posted_by', 'is_resolved', 'created_at']
    list_filter = ['status', 'is_resolved', 'created_at']
    search_fields = ['title', 'description', 'location']
    list_editable = ['is_resolved']
    ordering = ['-created_at']
