"""Notification Service - NO TWILIO DEPENDENCY"""
from django.core.mail import send_mail
from django.conf import settings
from .models import Notification
import logging

logger = logging.getLogger(__name__)

class NotificationService:
    @staticmethod
    def create_notification(user, title, message, notification_type, channel='email'):
        notification = Notification.objects.create(
            user=user, title=title, message=message, 
            type=notification_type, channel=channel
        )
        NotificationService.send_notification(notification)
        return notification

    @staticmethod
    def send_notification(notification):
        try:
            if notification.channel in ['email', 'both'] and notification.user.email:
                NotificationService._send_email(notification)
            if notification.channel == 'sms':
                NotificationService._send_sms_placeholder(notification)
        except Exception as e:
            logger.error(f"Notification failed {notification.id}: {e}")

    @staticmethod
    def _send_email(notification):
        send_mail(
            subject=f"Blood Alert: {notification.title}",
            message=notification.message,
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com'),
            recipient_list=[notification.user.email],
            fail_silently=True,
        )

    @staticmethod
    def _send_sms_placeholder(notification):
        """SMS placeholder - prints to console"""
        print(f"📱 SMS: {notification.title} -> {notification.user.username}")