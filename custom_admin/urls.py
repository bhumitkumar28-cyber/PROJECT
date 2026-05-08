from django.urls import path
from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('donors/', views.manage_donors, name='manage_donors'),
    path('donors/<int:pk>/approve/', views.approve_donor, name='approve_donor'),
    path('donors/<int:pk>/reject/', views.reject_donor, name='reject_donor'),
    path('donors/<int:pk>/delete/', views.delete_donor, name='delete_donor'),
    
    path('requesters/', views.manage_requesters, name='manage_requesters'),
    path('requesters/<int:pk>/verify/', views.verify_requester, name='verify_requester'),
    
    path('donations/', views.manage_donations, name='manage_donations'),
    path('donations/<int:pk>/approve/', views.approve_donation, name='approve_donation'),
    
    path('blood-requests/', views.manage_blood_requests, name='manage_blood_requests'),
    path('blood-requests/<int:pk>/approve/', views.approve_blood_request, name='approve_blood_request'),
    
    path('blood-stock/', views.manage_blood_stock, name='manage_blood_stock'),
    
    path('reports/', views.generate_reports, name='reports'),
    path('reports/export/', views.export_reports, name='export_reports'),
   
]