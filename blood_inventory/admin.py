from django.contrib import admin
from .models import BloodStock, StockTransaction

@admin.register(BloodStock)
class BloodStockAdmin(admin.ModelAdmin):
    list_display = ['blood_group', 'quantity', 'low_stock_threshold', 'stock_status', 'status_text', 'last_updated']
    list_filter = ['blood_group', 'quantity', 'location']
    search_fields = ['blood_group']
    list_editable = ['low_stock_threshold', 'quantity']

@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ['blood_stock', 'action', 'units', 'balance_after', 'timestamp']
    list_filter = ['action', 'timestamp', 'blood_stock__blood_group']
    search_fields = ['reason', 'blood_stock__blood_group']
    date_hierarchy = 'timestamp'