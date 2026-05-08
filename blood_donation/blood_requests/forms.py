from django import forms
from .models import BloodRequest
from django.utils import timezone
from datetime import timedelta

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['blood_group', 'quantity', 'location', 'hospital_name', 
                 'patient_name', 'urgency', 'contact_number', 'description', 'deadline']
        widgets = {
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'hospital_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'urgency': forms.Select(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'deadline': forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set minimum deadline to 1 hour from now
        min_deadline = timezone.now() + timedelta(hours=1)
        self.fields['deadline'].widget.attrs['min'] = min_deadline.isoformat()
    
    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
        if deadline < timezone.now() + timedelta(hours=1):
            raise forms.ValidationError("Deadline must be at least 1 hour from now.")
        return deadline