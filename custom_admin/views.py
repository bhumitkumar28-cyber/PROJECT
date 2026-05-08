import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.utils import timezone
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from reportlab.pdfgen import canvas
import csv

# Assuming you have these models in your apps
from donor.models import Donor, Donation
from accounts.models import UserProfile  # Custom user profile model
from blood_requests.models import BloodRequest
from blood_inventory.models import BloodStock

def is_superuser(user):
    return user.is_authenticated and user.is_superuser


def reject_donor(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    donor.is_approved = False
    donor.save()
    messages.error(request, f'Donor {donor.user.get_full_name()} rejected!')
    return redirect('custom_admin:manage_donors')
@login_required
@user_passes_test(is_superuser)
def dashboard(request):
    total_donors = Donor.objects.count()
    pending_donors = Donor.objects.filter(is_approved=False).count()
    approved_donors = Donor.objects.filter(is_approved=True).count()
    
    # LOW STOCK ALERTS
    low_stock_alerts = BloodStock.objects.filter(quantity__lt=10)
    
    # AUTO-APPROVE
    auto_approve_eligible()
    
    recent_donations = Donation.objects.filter(
        approved=True
    ).select_related('donor__user').order_by('-donation_date')[:5]
    
    context = {
        'total_donors': total_donors,
        'pending_donors': pending_donors,
        'approved_donors': approved_donors,
        'recent_donations': recent_donations,
        'low_stock_alerts': low_stock_alerts,  # NEW
    }
    return render(request, 'custom_admin/dashboard.html', context)

def auto_approve_eligible():
    eligible = Donor.objects.filter(
        is_approved=False
    ).annotate(donation_count=Count('donations')).filter(donation_count__gte=3)
    eligible.update(is_approved=True)

# ADD THESE NEW VIEWS AT BOTTOM
@csrf_exempt
def bulk_action(request, model):
    data = json.loads(request.body)
    ids = data['ids']
    action = data['action']
    
    if model == 'donors':
        if action == 'approve':
            Donor.objects.filter(id__in=ids).update(is_approved=True)
        elif action == 'reject':
            Donor.objects.filter(id__in=ids).update(is_approved=False)
        elif action == 'delete':
            Donor.objects.filter(id__in=ids).delete()
    
    return JsonResponse({'status': 'success'})

def export_pdf_report(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, "🏥 BLOOD BANK REPORT")
    p.setFont("Helvetica", 12)
    p.drawString(100, 720, f"Total Donors: {Donor.objects.count()}")
    p.setFont("Helvetica", 12)
    p.drawString(100, 700, f"Approved: {Donor.objects.filter(is_approved=True).count()}")
    p.save()
    buffer.seek(0)
    
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    return response

def export_excel_report(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Donors"
    
    headers = ['Name', 'Email', 'Blood Group', 'Phone', 'Status']
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = Font(bold=True)
    
    for row, donor in enumerate(Donor.objects.select_related('user'), 2):
        ws.cell(row=row, column=1, value=donor.user.get_full_name())
        ws.cell(row=row, column=2, value=donor.user.email)
        ws.cell(row=row, column=3, value=donor.blood_group)
        ws.cell(row=row, column=4, value=donor.phone)
        ws.cell(row=row, column=5, value='Approved' if donor.is_approved else 'Pending')
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="donors.xlsx"'
    wb.save(response)
    return response

@login_required
@user_passes_test(is_superuser)
def manage_donors(request):
    donors = Donor.objects.select_related('user').all()
    return render(request, 'custom_admin/manage_donors.html', {'donors': donors})

@login_required
@user_passes_test(is_superuser)
def approve_donor(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    donor.is_approved = True
    donor.save()
    messages.success(request, f'Donor {donor.user.get_full_name()} approved successfully!')
    return redirect('custom_admin:manage_donors')

@login_required
@user_passes_test(is_superuser)
@login_required
@user_passes_test(is_superuser)
def delete_donor(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    donor.delete()
    messages.success(request, 'Donor deleted successfully!')
    return redirect('custom_admin:manage_donors')

@login_required
@user_passes_test(is_superuser)
def manage_requesters(request):
    requesters = UserProfile.objects.filter(user_type='requester')
    return render(request, 'custom_admin/manage_requesters.html', {'requesters': requesters})

@login_required
@user_passes_test(is_superuser)
def verify_requester(request, pk):
    requester = get_object_or_404(UserProfile, pk=pk)
    requester.is_verified = True
    requester.save()
    messages.success(request, f'Requester {requester.user.get_full_name()} verified!')
    return redirect('custom_admin:manage_requesters')

@login_required
@user_passes_test(is_superuser)
def manage_donations(request):
    donations = Donation.objects.select_related('donor__user').all()
    return render(request, 'custom_admin/manage_donations.html', {'donations': donations})

@login_required
@user_passes_test(is_superuser)
def approve_donation(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    donation.approved = True
    donation.save()
    messages.success(request, 'Donation approved successfully!')
    return redirect('custom_admin:manage_donations')

@login_required
@user_passes_test(is_superuser)
def manage_blood_requests(request):
    requests = BloodRequest.objects.select_related('requester__user').all()
    return render(request, 'custom_admin/manage_blood_requests.html', {'requests': requests})

@login_required
@user_passes_test(is_superuser)
def approve_blood_request(request, pk):
    blood_request = get_object_or_404(BloodRequest, pk=pk)
    blood_request.status = 'approved'
    blood_request.save()
    messages.success(request, 'Blood request approved successfully!')
    return redirect('custom_admin:manage_blood_requests')

@login_required
@user_passes_test(is_superuser)
def manage_blood_stock(request):
    stock = BloodStock.objects.all()
    return render(request, 'custom_admin/manage_blood_stock.html', {'stock': stock})

@login_required
@user_passes_test(is_superuser)
def generate_reports(request):
    # Monthly donation stats
    monthly_donations = Donation.objects.filter(
        approved=True,
        donation_date__year=timezone.now().year
    ).extra({'month': "strftime('%%m', donation_date)"}).values('month').annotate(count=Count('id'))
    
    context = {
        'monthly_donations': monthly_donations,
    }
    return render(request, 'custom_admin/reports.html', context)

@login_required
@user_passes_test(is_superuser)
def export_reports(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="blood_bank_report.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Donor Name', 'Blood Group', 'Donation Date', 'Quantity'])
    
    donations = Donation.objects.select_related('donor__user').filter(approved=True)
    for donation in donations:
        writer.writerow([
            donation.donor.user.get_full_name(),
            donation.donor.blood_group,
            donation.donation_date,
            donation.quantity
        ])
    
    return response