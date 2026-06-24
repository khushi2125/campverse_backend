from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Notice
from .serializers import NoticeSerializer, NoticeCreateSerializer


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    
    def get_serializer_class(self):
        if self.action == 'create':
            return NoticeCreateSerializer
        return NoticeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'active']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'])
    def active(self, request):
        notices = Notice.objects.filter(is_active=True)
        serializer = self.get_serializer(notices, many=True)
        return Response(serializer.data)
