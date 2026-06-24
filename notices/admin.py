# Admin configuration for the notices application, registering the Notice model with the Django admin interface to allow for easy management of notices. The admin class includes customizations for list display, filtering, searching, and ordering of notices in the admin panel, as well as making the is_pinned and is_active fields editable directly from the list view for convenience.
from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'is_pinned', 'is_active', 'created_at']
    list_filter = ['category', 'is_pinned', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_pinned', 'is_active']
    ordering = ['-is_pinned', '-created_at']
