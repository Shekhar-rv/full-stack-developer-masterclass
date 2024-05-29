from django.apps import AppConfig


class CarsConfig(AppConfig):
    """
    Config class that helps Django install the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
