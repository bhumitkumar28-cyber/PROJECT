from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import BloodRequest
from .forms import BloodRequestForm

def request_list(request):
    """View all blood requests"""
    requests = BloodRequest.objects.filter(status='pending').select_related('user')
    paginator = Paginator(requests, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blood_requests/request_list.html', {'page_obj': page_obj})

def request_detail(request, pk):
    """Blood request detail page"""
    request_obj = get_object_or_404(BloodRequest, pk=pk)
    return render(request, 'blood_requests/request_detail.html', {'request': request_obj})

@login_required
def my_requests(request):
    """User's own blood requests"""
    requests = BloodRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'blood_requests/my_requests.html', {'requests': requests})

@login_required
def create_request(request):
    """Create new blood request"""
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.user = request.user
            blood_request.save()
            messages.success(request, 'Blood request created successfully!')
            return redirect('blood_request_detail', pk=blood_request.pk)
    else:
        form = BloodRequestForm()
    return render(request, 'blood_requests/create_request.html', {'form': form})

@login_required
def update_status(request, pk):
    """Update request status (fulfilled/cancelled)"""
    blood_request = get_object_or_404(BloodRequest, pk=pk)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['fulfilled', 'cancelled']:
            blood_request.status = status
            blood_request.save()
            messages.success(request, f'Request marked as {blood_request.get_status_display().lower()}')
        return redirect('blood_request_detail', pk=pk)
    
    return render(request, 'blood_requests/update_status.html', {
        'request': blood_request
    })