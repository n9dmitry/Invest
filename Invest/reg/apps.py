from django.apps import AppConfig


class RegConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reg'

class RegConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reg'

    def ready(self):
        import reg.signals