from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

class NotificationType(models.TextChoices):
    NEW_REQUEST = 'new_request', 'New Blood Request'
    MATCHING_DONOR = 'matching_donor', 'Matching Donor Found'
    LOW_STOCK = 'low_stock', 'Low Stock Alert'
    DONATION_CONFIRMED = 'donation_confirmed', 'Donation Confirmed'

class NotificationChannel(models.TextChoices):
    EMAIL = 'email', 'Email'
    SMS = 'sms', 'SMS'
    BOTH = 'both', 'Email + SMS'

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    message = models.TextField()
    type = models.CharField(max_length=20, choices=NotificationType.choices)
    channel = models.CharField(max_length=10, choices=NotificationChannel.choices, default=NotificationChannel.EMAIL)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.user.username}"

class NotificationPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='notification_prefs')
    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    new_request = models.BooleanField(default=True)
    matching_donor = models.BooleanField(default=True)
    low_stock = models.BooleanField(default=True)
    donation_confirmed = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Prefs for {self.user.username}"