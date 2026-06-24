# Views for the lost and found application, defining the LostFoundItemViewSet which provides API endpoints for managing lost and found items. The viewset allows for creating, retrieving, updating, and deleting lost and found items, and it includes custom logic for filtering items based on their status (lost or found) through query parameters. The viewset also ensures that the user who posted an item is automatically set when creating a new item through the API.
from rest_framework import viewsets, permissions
from .models import LostFoundItem
from .serializers import LostFoundItemSerializer


class LostFoundItemViewSet(viewsets.ModelViewSet):
    queryset = LostFoundItem.objects.all()
    serializer_class = LostFoundItemSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        
        if status and status != 'All':
            queryset = queryset.filter(status=status)
            
        return queryset
