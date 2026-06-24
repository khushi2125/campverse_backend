# Views for the marketplace application, defining the ItemViewSet which provides API endpoints for managing marketplace items. The viewset allows for creating, retrieving, updating, and deleting marketplace items, and it includes custom logic for filtering items based on category and status through query parameters. The viewset also ensures that the user who posted an item is automatically set when creating a new item through the API, and it includes logging for successful item creation and validation errors.
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Item
from .serializers import ItemSerializer, ItemCreateSerializer
import logging

logger = logging.getLogger(__name__)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return ItemCreateSerializer
        return ItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            logger.info(f"Successfully created item: {serializer.data}")
            return Response(serializer.data, status=201, headers=headers)
        except ValidationError as e:
            logger.error(f"Validation error creating item: {e.detail}")
            logger.error(f"Request data was: {request.data}")
            raise
    
    def perform_create(self, serializer):
        # Save with seller if authenticated, otherwise without
        if self.request.user.is_authenticated:
            serializer.save(seller=self.request.user)
        else:
            serializer.save()

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        status = self.request.query_params.get('status')
        
        if category and category != 'All':
            queryset = queryset.filter(category=category)
        if status:
            queryset = queryset.filter(status=status)
        else:
            queryset = queryset.filter(status='Available')
            
        return queryset
