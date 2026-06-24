# Admin configuration for the college application, registering models such as Course, Faculty, Timetable, Attendance, and Fee with the Django admin interface to allow for easy management of these entities. Each model has customized list displays, search fields, and filters to enhance the admin experience.
from django.contrib import admin
from .models import Course, Faculty, Timetable, Attendance, Fee

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'credits', 'students', 'fees', 'created_at']
    search_fields = ['name']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'department', 'email', 'phone']
    search_fields = ['name', 'subject', 'department']

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ['day', 'course', 'slot', 'room', 'faculty']
    list_filter = ['day', 'course']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['date', 'course', 'present', 'total', 'status']
    list_filter = ['date', 'course', 'status']

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'course', 'amount', 'status', 'date']
    list_filter = ['status', 'course', 'date']
    search_fields = ['student_name']
