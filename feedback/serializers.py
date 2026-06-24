from rest_framework import serializers
from django.utils import timezone
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    anonymous = serializers.BooleanField(source='is_anonymous', read_only=True)
    time_ago = serializers.SerializerMethodField()
    
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'anonymous', 'feedback_type', 'target_name', 'rating', 'comment', 'created_at', 'time_ago']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    
    def get_time_ago(self, obj):
        delta = timezone.now() - obj.created_at
        if delta.seconds < 60:
            return "Just now"
        elif delta.seconds < 3600:
            return f"{delta.seconds // 60} min ago"
        elif delta.days == 0:
            return f"{delta.seconds // 3600} hr ago"
        elif delta.days == 1:
            return "1 day ago"
        else:
            return f"{delta.days} days ago"


class FeedbackCreateSerializer(serializers.ModelSerializer):
    anonymous = serializers.BooleanField(write_only=True, default=False, source='is_anonymous')
    
    class Meta:
        model = Feedback
        fields = ['feedback_type', 'target_name', 'rating', 'comment', 'anonymous']
