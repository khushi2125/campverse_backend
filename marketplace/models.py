# Models for the marketplace application, defining the Item model which includes fields for title, description, category, condition, price, old price, seller (linked to the user model), location, image, tags, status (available, sold, pending), and timestamps for creation and updates. The model also includes choices for category, condition, and status to ensure data consistency, as well as a string representation method and meta options for ordering items by creation date.
from django.db import models
from django.conf import settings


class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Books', 'Books'),
        ('Furniture', 'Furniture'),
        ('Sports', 'Sports'),
        ('Clothing', 'Clothing'),
    ]
    
    CONDITION_CHOICES = [
        ('Like New', 'Like New'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    ]
    
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
        ('Pending', 'Pending'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='Good')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    location = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='marketplace_images/', blank=True, null=True)
    tags = models.JSONField(default=list, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
