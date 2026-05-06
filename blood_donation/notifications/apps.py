from django.apps import AppConfig

class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'

    def ready(self):
        # Safe import - won't crash
        try:
            import notifications.signals
        except ImportError:
            pass