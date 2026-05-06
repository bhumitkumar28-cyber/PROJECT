from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Notification, NotificationPreference
from .forms import NotificationPreferenceForm
from .services import NotificationService

@login_required
def notifications_list(request):
    notifications = Notification.objects.filter(user=request.user).select_related('user')
    unread = notifications.filter(is_read=False).count()
    return render(request, 'notifications/list.html', {
        'notifications': notifications, 'unread_count': unread
    })

@login_required
def notifications_settings(request):
    pref, _ = NotificationPreference.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = NotificationPreferenceForm(request.POST, instance=pref)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings saved!')
            return redirect('notifications_settings')
    else:
        form = NotificationPreferenceForm(instance=pref)
    return render(request, 'notifications/settings.html', {'form': form})

@csrf_exempt
@login_required
def mark_read(request):
    if request.method == 'POST':
        nid = request.POST.get('id')
        Notification.objects.filter(id=nid, user=request.user).update(
            is_read=True, read_at=timezone.now()
        )
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid'}, status=400)

@login_required
def unread_count(request):
    count = Notification.objects.filter(user=request.user, is_read=False).count()
    return JsonResponse({'count': count})