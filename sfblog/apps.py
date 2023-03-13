from django.apps import AppConfig


class SfblogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sfblog'

    def ready(self):
        import sfblog.signals
