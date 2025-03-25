from django.apps import AppConfig

class DestinationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'destinations'  # Keep this as the correct app name
    label = 'destinations'  # Change this back to 'destinations'
