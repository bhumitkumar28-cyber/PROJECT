# donor/forms.py
from django import forms
from .models import Donation
from datetime import date
from .models import Donor  # Add this line
# Also import Donation if used similarly
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['date', 'units', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}),
            'units': forms.NumberInput(attrs={'min': 1, 'max': 2}),
        }

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['available']
        widgets = {
            'available': forms.CheckboxInput(),
        }
