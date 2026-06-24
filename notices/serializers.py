# Serializers for the notices application, converting Notice model instances to JSON format for API responses and validating input data for creating and updating notices through the API endpoints. The serializers include custom fields to display the name of the author and a method to calculate how long ago a notice was posted. The NoticeCreateSerializer is used specifically for creating new notices, allowing for input of title, description, category, pinned status, and active status.
from rest_framework import serializers
from django.utils import timezone
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    time_ago = serializers.SerializerMethodField()

    
    class Meta:
        model = Notice
        fields = ['id', 'title', 'description', 'category', 'author', 'author_name', 'is_pinned', 'is_active', 'created_at', 'updated_at', 'time_ago']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def get_time_ago(self, obj):
        delta = timezone.now() - obj.created_at
        if delta.seconds < 3600:
            return f"{delta.seconds // 60} min ago"
        elif delta.days == 0:
            return f"{delta.seconds // 3600} hr ago"
        else:
            return f"{delta.days} day(s) ago"


class NoticeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['title', 'description', 'category', 'is_pinned', 'is_active']
