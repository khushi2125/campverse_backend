# URL configuration for the lost and found application, defining API endpoints for managing lost and found items using Django REST Framework's DefaultRouter. The router registers the LostFoundItemViewSet, which provides CRUD operations for lost and found items, allowing users to create, retrieve, update, and delete items through the API. The urlpatterns include the router's URLs to make these endpoints accessible.
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.LostFoundItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
