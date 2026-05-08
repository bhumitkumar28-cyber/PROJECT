# blood_inventory/urls.py
from django.urls import path
from . import views

app_name = 'blood_inventory'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('update/', views.update_stock, name='update_stock'),
    path('history/', views.history, name='history'),
    path('alerts/', views.low_stock_alerts, name='low_stock_alerts'),  # ← ADD THIS
]