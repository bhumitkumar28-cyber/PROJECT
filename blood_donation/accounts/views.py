from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  # ✅ Added decode
from django.utils.encoding import force_bytes, force_str  # ✅ Added force_str
from django.contrib.auth.tokens import default_token_generator 
from django.conf import settings  
from django.urls import reverse  
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from donor.models import Donor, DonorProfile  # ✅ Added for donor signup
from .forms import (
    DonorSignupForm, RequesterSignupForm, 
    CustomAuthenticationForm, ProfileForm, 
    UserProfileForm, PasswordResetForm, SetPasswordForm  
)
from .models import UserProfile

def user_type_selection(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    return render(request, 'accounts/user_type_selection.html')

def donor_signup(request):
    if request.method == 'POST':
        form = DonorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            # ✅ Create Donor profile
            Donor.objects.create(
                user=user,
                phone=form.cleaned_data.get('phone_number', ''),
                blood_group=form.cleaned_data.get('blood_group', ''),
                city=form.cleaned_data.get('city', 'Agra'),
                address=form.cleaned_data.get('address', ''),
                date_of_birth=form.cleaned_data.get('date_of_birth'),
            )
            
            # ✅ Create DonorProfile
            DonorProfile.objects.create(
                user=user,
                phone_number=form.cleaned_data.get('phone_number', ''),
                blood_group=form.cleaned_data.get('blood_group', ''),
                city=form.cleaned_data.get('city', 'Agra'),
                address=form.cleaned_data.get('address', ''),
                date_of_birth=form.cleaned_data.get('date_of_birth'),
            )
            
            messages.success(request, 'Account created successfully! Welcome Donor!')
            return redirect('core:dashboard')
    else:
        form = DonorSignupForm()
    return render(request, 'accounts/donor_signup.html', {'form': form})

def requester_signup(request):
    if request.method == 'POST':
        form = RequesterSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome Requester!')
            return redirect('core:dashboard')
    else:
        form = RequesterSignupForm()
    return render(request, 'accounts/requester_signup.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    # ✅ FIX: Initialize form FIRST for GET requests
    form = CustomAuthenticationForm()
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name() or user.username}!')
            next_url = request.POST.get('next', 'core:dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('accounts:user_type_selection')
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)  # ✅ Now User is imported
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_url = f"{request.scheme}://{request.get_host()}/accounts/reset/{uid}/{token}/"
                
                send_mail(
                    'Password Reset - Blood Bank',
                    f'Click this link to reset your password: {reset_url}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Password reset email sent! Check your console/terminal.')
                return redirect('accounts:login')
            except User.DoesNotExist:
                messages.error(request, 'No account found with that email.')
    else:
        form = PasswordResetForm()
    return render(request, 'accounts/password_reset.html', {'form': form})

def password_reset_confirm(request, uidb64, token):
    # Handle malformed UID64 (remove = or %3D)
    clean_uidb64 = uidb64.lstrip('=%3D')
    
    user = None
    try:
        uid = force_str(urlsafe_base64_decode(clean_uidb64))
        user = User.objects.get(pk=uid)
    except:
        pass
    
    # Invalid token/user
    if not user or not default_token_generator.check_token(user, token):
        messages.error(request, 'Invalid or expired reset link')
        return redirect('accounts:login')
    
    # Process form
    if request.method == 'POST':
        # ✅ FIXED: Correct SetPasswordForm syntax
        form = SetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Password reset successful! You can login now.')
            return redirect('accounts:login')
    else:
        form = SetPasswordForm(user=user)
    
    return render(request, 'accounts/password_reset_confirm.html', {'form': form})
@login_required
def profile(request):
    # ✅ SUPER SAFE - Creates profile if missing
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'user_type': 'donor', 'city': 'Agra'}
    )
    
    if request.method == 'POST':
        profile.phone_number = request.POST.get('phone_number', '')
        profile.blood_group = request.POST.get('blood_group', '')
        profile.address = request.POST.get('address', '')
        profile.city = request.POST.get('city', 'Agra')
        profile.save()
        messages.success(request, '✅ Profile updated!')
        return redirect('accounts:profile')
    
    context = {
        'profile': profile,
        'user_type': profile.user_type,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('core:dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})