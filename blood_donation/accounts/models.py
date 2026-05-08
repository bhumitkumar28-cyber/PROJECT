from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    USER_TYPES = [
        ('donor', 'Donor'),
        ('requester', 'Requester'),
    ]
    
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='accounts_profile'  # ✅ Unique related_name
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    city = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=17, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"