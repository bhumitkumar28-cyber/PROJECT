# donor/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Donor, Donation
from .forms import DonationForm, AvailabilityForm
from django.shortcuts import render, redirect

from django.contrib import messages
from django.db import transaction
from .models import DonorProfile  # Your existing model
from notifications.models import Notification
from notifications.services import NotificationService
class PublicDonorListView(ListView):
    model = Donor
    template_name = 'donor/donor_list.html'
    context_object_name = 'donors'
    paginate_by = 10

    def get_queryset(self):
        return Donor.objects.filter(available=True).select_related('user')

class DonorDetailView(DetailView):
    model = Donor
    template_name = 'donor/donor_detail.html'
    context_object_name = 'donor'
    pk_url_kwarg = 'pk'


@login_required
def dashboard(request):
    # SAFE PROFILE ACCESS - Auto-create if missing
    donor_profile, created = DonorProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'blood_type': 'O+',
            'phone_number': request.user.email.split('@')[0] + '@example.com',
            'location': 'Default City',
        }
    )
    
    if created:
        messages.success(request, "Welcome! Donor profile created.")
    
    # Notification count
    unread_count = Notification.objects.filter(
        user=request.user, is_read=False
    ).count()
    
    context = {
        'donor_profile': donor_profile,
        'unread_notifications': unread_count,
        'donations_count': DonorProfile.objects.filter(user=request.user).count(),  # or your logic
    }
    return render(request, 'donor/dashboard.html', context)

@login_required
def donation_history(request):
    donor = request.user.donor_profile
    donations = donor.donations.all().order_by('-date')
    return render(request, 'donor/donation_history.html', {'donations': donations})

@login_required
def add_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donor = request.user.donor_profile
            if donor.last_donation:
                last_date = donor.last_donation
            else:
                last_date = date.today()
            if (donation.date - last_date).days >= 90:  # 3 months gap
                donation.donor = donor
                donation.save()
                donor.last_donation = donation.date
                donor.save()
                return redirect('donor:dashboard')
    else:
        form = DonationForm()
    return render(request, 'donor/add_donation.html', {'form': form})

@login_required
def update_availability(request):
    donor = request.user.donor_profile
    if request.method == 'POST':
        form = AvailabilityForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor:dashboard')
    else:
        form = AvailabilityForm(instance=donor)
    return render(request, 'donor/update_availability.html', {'form': form})
class DonorSearchView(ListView):
    model = Donor
    template_name = 'donor/search.html'
    context_object_name = 'donors'
    paginate_by = 10

    def get_queryset(self):
        queryset = Donor.objects.filter(available=True)
        blood_group = self.request.GET.get('blood_group')
        location = self.request.GET.get('location')
        if blood_group:
            queryset = queryset.filter(blood_group=blood_group)
        if location:
            queryset = queryset.filter(location__icontains=location)
        return queryset
