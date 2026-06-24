# apps.py for the college application, defining the CollegeConfig class which specifies the default auto field type and the name of the application. This configuration is used by Django to set up the application correctly when it is included in the project.
from django.apps import AppConfig
class CollegeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'college'
