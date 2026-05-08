from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class UserProfile(models.Model):
    USER_TYPES = (
        ('donor', 'Donor'),
        ('requester', 'Requester'),
        ('admin', 'Admin'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    phone = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    last_donation_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Donor(models.Model):
    BLOOD_GROUPS = (
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='core_donor')
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    city = models.CharField(max_length=100)
    weight = models.FloatField()
    age = models.IntegerField()
    availability_date = models.DateField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Requester(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='core_requester')
    hospital_name = models.CharField(max_length=200)
    hospital_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class BloodRequest(models.Model):
    requester = models.ForeignKey(Requester, on_delete=models.CASCADE, related_name='requests')
    blood_group = models.CharField(max_length=5, choices=Donor.BLOOD_GROUPS)
    units_required = models.IntegerField()
    urgency = models.CharField(max_length=20, default='normal')
    location = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('fulfilled', 'Fulfilled'),
        ('cancelled', 'Cancelled'),
    ), default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    fulfilled_date = models.DateTimeField(null=True, blank=True)

class Donation(models.Model):
    donor = models.ForeignKey('Donor', on_delete=models.CASCADE, related_name='donations')
    blood_group = models.CharField(max_length=5)
    units_donated = models.IntegerField()
    donation_date = models.DateField()
    collection_center = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)

class BloodStock(models.Model):
    blood_group = models.CharField(max_length=5, choices=Donor.BLOOD_GROUPS)
    units_available = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

class StockHistory(models.Model):
    blood_group = models.CharField(max_length=5)
    units_added = models.IntegerField()
    units_removed = models.IntegerField(default=0)
    reason = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core_notifications')  # ✅ FINAL FIX
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)