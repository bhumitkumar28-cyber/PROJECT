from django import forms
from .models import BloodStock, StockTransaction

class StockUpdateForm(forms.Form):
    blood_group = forms.ChoiceField(choices=BloodStock.BLOOD_GROUPS)
    action = forms.ChoiceField(choices=[('IN', 'Add Stock'), ('OUT', 'Issue Stock')])
    units = forms.IntegerField(min_value=1, max_value=1000)
    reason = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'rows': 3}))