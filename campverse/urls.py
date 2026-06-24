# URL configuration for the CampVerse project, routing API endpoints for authentication, notices, marketplace, lost and found, college, and feedback applications. It also serves media files during development when DEBUG is True.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/notices/', include('notices.urls')),
    path('api/marketplace/', include('marketplace.urls')),
    path('api/lostfound/', include('lostfound.urls')),
    path('api/college/', include('college.urls')),
    path('api/feedback/', include('feedback.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
