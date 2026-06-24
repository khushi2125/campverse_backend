# URL configuration for the marketplace application, defining API endpoints for managing marketplace items using Django REST Framework's DefaultRouter. The router registers the ItemViewSet, which provides CRUD operations for marketplace items, allowing users to create, retrieve, update, and delete items through the API. The urlpatterns include the router's URLs to make these endpoints accessible.
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
