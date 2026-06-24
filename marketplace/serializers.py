# Serializers for the marketplace application, converting Item model instances to JSON format for API responses and validating input data for creating and updating marketplace items through the API endpoints. The serializers include custom fields to display the name and email of the seller, as well as a method to calculate how long ago an item was posted. The ItemCreateSerializer also includes custom logic to handle optional fields like old_price and tags, allowing for flexible input formats when creating new items through the API.
from rest_framework import serializers
from django.utils import timezone
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.get_full_name', read_only=True)
    seller_email = serializers.EmailField(source='seller.email', read_only=True)
    posted = serializers.SerializerMethodField()
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'category', 'condition', 'price', 'old_price', 'seller', 'seller_name', 'seller_email', 'location', 'image', 'tags', 'status', 'created_at', 'updated_at', 'posted']
        read_only_fields = ['id', 'seller', 'status', 'created_at', 'updated_at']

    def get_posted(self, obj):
        delta = timezone.now() - obj.created_at
        if delta.seconds < 3600:
            return f"{delta.seconds // 60} min ago"
        elif delta.days == 0:
            return f"{delta.seconds // 3600} hr ago"
        elif delta.days == 1:
            return "1 day ago"
        else:
            return f"{delta.days} days ago"


class ItemCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    old_price = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    tags = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = Item
        fields = ['title', 'description', 'category', 'condition', 'price', 'old_price', 'location', 'image', 'tags']
    
    def to_internal_value(self, data):
        # Convert form data to proper types before validation
        ret = super().to_internal_value(data)
        
        # Handle old_price
        if 'old_price' in ret:
            if ret['old_price'] is None or ret['old_price'] == '' or ret['old_price'] == 'null':
                ret['old_price'] = None
        
        # Handle tags - convert comma-separated string to list
        if 'tags' in ret:
            if ret['tags'] is None or ret['tags'] == '':
                ret['tags'] = []
            elif isinstance(ret['tags'], str):
                ret['tags'] = [tag.strip() for tag in ret['tags'].split(',') if tag.strip()]
        
        return ret
    
    def create(self, validated_data):
        return super().create(validated_data)
