# URL configuration for the college application, defining API endpoints for courses, faculty, timetable, attendance, and fees using Django REST Framework's DefaultRouter.
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('faculty', views.FacultyViewSet)
router.register('timetable', views.TimetableViewSet)
router.register('attendance', views.AttendanceViewSet)
router.register('fees', views.FeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
