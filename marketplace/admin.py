# Admin configuration for the marketplace application, registering the Item model with the Django admin interface to allow for easy management of marketplace items. The admin class includes customizations for list display, filtering, searching, and ordering of items in the admin panel, as well as making the status field editable directly from the list view for convenience.
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'condition', 'price', 'seller', 'status', 'created_at']
    list_filter = ['category', 'condition', 'status', 'created_at']
    search_fields = ['title', 'description', 'seller__username']
    list_editable = ['status']
    ordering = ['-created_at']
