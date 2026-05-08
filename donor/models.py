# donor/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

BLOOD_GROUPS = (
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('A+', 'A+'),
    ('B-', 'B-'),
    ('B+', 'B+'),
    ('AB-', 'AB-'),
    ('AB+', 'AB+'),
)

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='donor')  # ✅ Changed
    phone = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    city = models.CharField(max_length=100, default='Agra')
    address = models.TextField()
    date_of_birth = models.DateField()
    last_donation = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.blood_group})"

    def get_absolute_url(self):
        return reverse('donor:detail', kwargs={'pk': self.pk})

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='donations')
    date = models.DateField()
    units = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):  # ✅ Fixed this too
        return f"{self.donor} - {self.date} ({self.units} units)"

class DonorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='donor_profile'  # ✅ Keep this one
    )
    address = models.CharField(max_length=255)

    def __str__(self):  # ✅ Fixed this too
        return f"{self.user.get_full_name()} - Profile"