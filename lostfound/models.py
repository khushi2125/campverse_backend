# Models for the lost and found application, defining the LostFoundItem model which includes fields for title, description, status (lost or found), location, date, contact information, image, and metadata such as the user who posted the item and timestamps for creation and updates. The model also includes a string representation method and meta options for ordering items by creation date.
from django.db import models
from django.conf import settings

class LostFoundItem(models.Model):
    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    location = models.CharField(max_length=255)
    date = models.DateField()
    contact_info = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='lostfound_images/', blank=True, null=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lostfound_items')
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.status})"
