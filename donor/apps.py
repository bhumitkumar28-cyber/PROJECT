from django.apps import AppConfig

class DonerMgmtConfig(AppConfig):  # Or rename class to DonorConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'donor'  # Must be 'donor', not 'doner_mgmt'
