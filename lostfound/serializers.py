# Serializers for the lost and found application, converting LostFoundItem model instances to JSON format for API responses and validating input data for creating and updating lost and found items through the API endpoints. The serializer includes a custom field to display the name of the user who posted the item, and it specifies which fields are read-only to ensure data integrity.
from rest_framework import serializers
from .models import LostFoundItem


class LostFoundItemSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.CharField(source='posted_by.get_full_name', read_only=True)

    class Meta:
        model = LostFoundItem
        fields = ['id', 'title', 'description', 'status', 'location', 'date', 'contact_info', 'image', 'posted_by', 'posted_by_name', 'is_resolved', 'created_at', 'updated_at']
        read_only_fields = ['id', 'posted_by', 'is_resolved', 'created_at', 'updated_at']
