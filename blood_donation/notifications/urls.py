from django.urls import path
from . import views

app_name = 'notifications'
urlpatterns = [
    path('', views.notifications_list, name='list'),
    path('settings/', views.notifications_settings, name='settings'),
    path('mark-read/', views.mark_read, name='mark_read'),
    path('count/', views.unread_count, name='count'),
]