from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import BloodStock

@receiver(post_save, sender=BloodStock)
def low_stock_email_alert(sender, instance, **kwargs):
    if instance.quantity <= instance.low_stock_threshold:
        subject = f"LOW STOCK ALERT: {instance.blood_group}"
        message = f"{instance.blood_group} stock is now {instance.quantity} units (threshold: {instance.low_stock_threshold})"
        
        send_mail(
            subject,
            message,
            'inventory@bloodbank.com',
            ['admin@bloodbank.com'],
            fail_silently=True,
        )