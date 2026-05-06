# donor/urls.py
from django.urls import path
from . import views

app_name = 'donor'

urlpatterns = [
    path('', views.PublicDonorListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.DonorDetailView.as_view(), name='detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('history/', views.donation_history, name='history'),
    path('add-donation/', views.add_donation, name='add_donation'),
    path('availability/', views.update_availability, name='update_availability'),
]
