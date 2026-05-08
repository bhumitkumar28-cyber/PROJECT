"""Safe signals - won't break if other models don't exist"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.apps import apps
from .services import NotificationService
from .models import NotificationPreference

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_prefs(sender, instance, created, **kwargs):
    if created:
        NotificationPreference.objects.get_or_create(user=instance)

# Safe model checks
BloodRequest = apps.get_model('requests', 'BloodRequest', require_ready=False) if apps.is_installed('requests') else None
BloodStock = apps.get_model('blood_inventory', 'BloodStock', require_ready=False) if apps.is_installed('blood_inventory') else None

if BloodRequest:
    @receiver(post_save, sender=BloodRequest)
    def new_request_alert(sender, instance, created, **kwargs):
        if created:
            users = User.objects.filter(notification_prefs__new_request=True)
            for user in users:
                NotificationService.create_notification(
                    user=user, title=f"🩸 New: {instance.blood_type}",
                    message=f"Request at {getattr(instance, 'location', 'your area')}",
                    notification_type='new_request'
                )

if BloodStock:
    @receiver(post_save, sender=BloodStock)
    def low_stock_alert(sender, instance, **kwargs):
        if getattr(instance, 'quantity', 999) < 5:
            admins = User.objects.filter(is_staff=True)
            for admin in admins:
                NotificationService.create_notification(
                    admin, f"⚠️ LOW: {getattr(instance, 'blood_type', 'Blood')}",
                    f"Only {getattr(instance, 'quantity', 0)} units left!",
                    'low_stock'
                )