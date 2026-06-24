# Views for the feedback application, defining the FeedbackViewSet which provides API endpoints for managing feedback entries. The viewset allows for creating, retrieving, updating, and deleting feedback entries, and it includes custom logic for linking feedback to authenticated users when submitted without anonymity. The viewset also uses different serializers for creating feedback versus retrieving feedback to handle the different data requirements for these operations.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Feedback
from .serializers import FeedbackSerializer, FeedbackCreateSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return FeedbackCreateSerializer
        return FeedbackSerializer
    
    def perform_create(self, serializer):
        # If user is authenticated and not submitting anonymously, link to user
        if self.request.user.is_authenticated and not self.request.data.get('anonymous', False):
            serializer.save(user=self.request.user)
        else:
            serializer.save(user=None)
