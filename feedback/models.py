# Models for the feedback application, defining the Feedback model which includes fields for user (linked to the user model), feedback type, target name, rating, comment, anonymity flag, and timestamps for creation and updates. The model also includes choices for feedback type and rating to ensure data consistency, as well as a string representation method and meta options for ordering feedback entries by creation date.
from django.db import models
from django.conf import settings

class Feedback(models.Model):
    FEEDBACK_TYPES = [
        ('course', 'Course/Academic'),
        ('teacher', 'Teacher/Staff'),
        ('hostel', 'Hostel/Facilities'),
        ('cafeteria', 'Cafeteria'),
        ('sports', 'Sports'),
        ('admin', 'Administrative'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPES)
    target_name = models.CharField(max_length=255)  # Category or specific target
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 stars
    comment = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Feedback by {self.user.username if self.user and not self.is_anonymous else 'Anonymous'} - {self.target_name}"
