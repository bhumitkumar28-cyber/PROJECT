from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.user_type_selection, name='user_type_selection'),
    path('signup/donor/', views.donor_signup, name='donor_signup'),
    path('signup/requester/', views.requester_signup, name='requester_signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    # NEW PASSWORD RESET URLS
    path('password-reset/', views.password_reset, name='password_reset'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
]