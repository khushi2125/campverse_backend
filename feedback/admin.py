# Admin configuration for the feedback application, registering the Feedback model with the Django admin interface to allow for easy management of feedback entries. The admin class includes customizations for list display, filtering, searching, and ordering of feedback entries in the admin panel, as well as making the created_at and updated_at fields read-only to prevent accidental modifications.
from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'target_name', 'feedback_type', 'rating', 'is_anonymous', 'created_at']
    list_filter = ['feedback_type', 'rating', 'is_anonymous', 'created_at']
    search_fields = ['comment', 'target_name']
    readonly_fields = ['created_at', 'updated_at']
