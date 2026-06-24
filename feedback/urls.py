# URL configuration for the feedback application, defining API endpoints for managing feedback entries using Django REST Framework's DefaultRouter. The router registers the FeedbackViewSet, which provides CRUD operations for feedback entries, allowing users to create, retrieve, update, and delete feedback through the API. The urlpatterns include the router's URLs to make these endpoints accessible.
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
