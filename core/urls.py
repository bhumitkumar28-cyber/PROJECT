from django.urls import path
from . import views

app_name = 'core'  # ✅ Already good

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'), 
    path('how_it_works/', views.how_it_works, name='how_it_works'),
    path('dashboard/', views.dashboard, name='dashboard'),  # ✅ ADD THIS LINE
]