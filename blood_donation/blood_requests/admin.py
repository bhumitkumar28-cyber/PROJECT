from django.contrib import admin
from .models import BloodRequest

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'blood_group', 'quantity', 'status', 'location', 'created_at', 'is_overdue']
    list_filter = ['status', 'blood_group', 'urgency', 'created_at']
    search_fields = ['patient_name', 'location', 'hospital_name']
    readonly_fields = ['created_at', 'updated_at']