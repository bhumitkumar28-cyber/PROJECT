from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, Donor, Requester, BloodRequest

class DonorSignupForm(UserCreationForm):
    blood_group = forms.CharField(max_length=5)
    city = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

class RequesterSignupForm(UserCreationForm):
    hospital_name = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=15)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['blood_group', 'units_required', 'urgency', 'location', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class DonorUpdateForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['blood_group', 'city', 'weight', 'age', 'availability_date', 'is_available']