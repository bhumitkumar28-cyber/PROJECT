from django.apps import AppConfig

class BloodInventoryConfig(AppConfig):
    name = 'blood_inventory'
    verbose_name = "Blood Inventory"
    default_auto_field = 'django.db.models.BigAutoField'
    
    def ready(self):
        # Optional: Email signals (create signals.py later)
        try:
            import blood_inventory.signals
        except ImportError:
            pass