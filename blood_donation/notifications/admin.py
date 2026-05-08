from django.contrib import admin
from .models import Notification, NotificationPreference, NotificationType

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'type', 'channel', 'is_read', 'created_at']
    list_filter = ['type', 'channel', 'is_read', 'created_at']
    search_fields = ['title', 'user__username']
    readonly_fields = ['id', 'created_at']

@admin.register(NotificationPreference)
class NotificationPreferenceAdmin(admin.ModelAdmin):
    list_display = ['user', 'email_notifications', 'sms_notifications', 'phone_number']
    search_fields = ['user__username']