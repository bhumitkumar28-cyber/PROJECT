from django.urls import path
from . import views

app_name = 'blood_requests'

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('create/', views.create_request, name='create_request'),
    path('request/<int:pk>/update-status/', views.update_status, name='update_status'),
]