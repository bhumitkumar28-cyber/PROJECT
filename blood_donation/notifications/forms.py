from django import forms
from .models import NotificationPreference

class NotificationPreferenceForm(forms.ModelForm):
    class Meta:
        model = NotificationPreference
        fields = ['email_notifications', 'sms_notifications', 'phone_number',
                 'new_request', 'matching_donor', 'low_stock', 'donation_confirmed']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': '+1-234-567-8900'}),
            'email_notifications': forms.CheckboxInput(),
            'sms_notifications': forms.CheckboxInput(),
        }