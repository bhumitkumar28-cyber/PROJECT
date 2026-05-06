from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile

# Your existing views (unchanged)
def about(request):
    return render(request, 'core/about.html')  # ✅ Changed from 'about.html'

def contact(request):
    return render(request, 'core/contact.html')  # ✅ Changed

def home(request):
    return render(request, 'core/home.html')  # ✅ Changed

def how_it_works(request):
    return render(request, 'core/how_it_works.html')

# ADD THIS NEW FUNCTION
@login_required
def dashboard(request):
    try:
        profile = request.user.accounts_profile
        user_type = profile.user_type
    except:
        user_type = 'unknown'
    
    context = {
        'user_type': user_type,
        'page_title': 'Dashboard'
    }
    return render(request, 'core/dashboard.html', context)