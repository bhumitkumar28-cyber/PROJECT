from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

BLOOD_GROUPS = [
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('fulfilled', 'Fulfilled'),
    ('cancelled', 'Cancelled'),
]

class BloodRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blood_requests')
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    quantity = models.PositiveIntegerField(help_text="Units required (1 unit = 350ml)")
    location = models.CharField(max_length=200)
    hospital_name = models.CharField(max_length=200)
    patient_name = models.CharField(max_length=100)
    urgency = models.CharField(
        max_length=20,
        choices=[('urgent', 'Urgent'), ('normal', 'Normal')],
        default='normal'
    )
    contact_number = models.CharField(max_length=15)
    description = models.TextField(blank=True, help_text="Additional information")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.patient_name} - {self.blood_group} - {self.get_status_display()}"
    
    def get_absolute_url(self):
        return reverse('blood_request_detail', kwargs={'pk': self.pk})
    
    def is_overdue(self):
        return timezone.now() > self.deadline and self.status == 'pending'
    
    def days_remaining(self):
        from datetime import timedelta
        if self.status != 'pending':
            return None
        remaining = self.deadline - timezone.now()
        return max(0, remaining.days)