# Models for the notices application, defining the Notice model which includes fields for title, description, category, author (linked to the user model), is_pinned, is_active, and timestamps for creation and updates. The model also includes choices for category to ensure data consistency, as well as a string representation method and meta options for ordering notices by pinned status and creation date.
from django.db import models
from django.conf import settings

class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('Academics', 'Academics'),
        ('General', 'General'),
        ('Hostel', 'Hostel'),
        ('Events', 'Events'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='General')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='notices')
    is_pinned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_pinned', '-created_at']

    def __str__(self):
        return self.title
