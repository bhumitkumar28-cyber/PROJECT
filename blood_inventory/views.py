from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, F
from .models import BloodStock, StockTransaction

def dashboard(request):
    stocks = BloodStock.objects.all()
    critical = stocks.filter(quantity__lte=2)
    low_stock = stocks.filter(quantity__gt=2, quantity__lte=F('low_stock_threshold'))
    
    context = {
        'stocks': stocks,
        'critical_alerts': critical,
        'low_stock_alerts': low_stock,
        'total_units': sum(s.quantity for s in stocks),
    }
    return render(request, 'blood_inventory/dashboard.html', context)

def update_stock(request):
    if request.method == 'POST':
        blood_group = request.POST['blood_group']
        action = request.POST['action']
        units = int(request.POST['units'])
        reason = request.POST['reason']
        
        stock, created = BloodStock.objects.get_or_create(
            blood_group=blood_group,
            defaults={'quantity': 0, 'low_stock_threshold': 5}
        )
        
        if action == 'IN':
            stock.quantity += units
        elif action == 'OUT':
            if stock.quantity >= units:
                stock.quantity -= units
            else:
                messages.error(request, f"Not enough {blood_group} stock!")
                all_groups = [
                    ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'),
                    ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')
                ]
                return render(request, 'blood_inventory/update_stock.html', {'all_groups': all_groups})
        
        stock.save()
        
        StockTransaction.objects.create(
            blood_stock=stock,
            action=action,
            units=units,
            balance_after=stock.quantity,
            reason=reason
        )
        
        action_text = "Added" if action == 'IN' else "Issued"
        messages.success(request, f"{action_text} {units} units of {blood_group}")
        return redirect('blood_inventory:dashboard')
    
    # HARDCODED - NO IMPORT DEPENDENCY
    all_groups = [
        ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ]
    context = {'all_groups': all_groups}
    return render(request, 'blood_inventory/update_stock.html', context)

def history(request):
    transactions = StockTransaction.objects.select_related('blood_stock').all()
    
    query = request.GET.get('q', '')
    if query:
        transactions = transactions.filter(
            Q(blood_stock__blood_group__icontains=query) |
            Q(reason__icontains=query)
        )
    
    paginator = Paginator(transactions, 25)
    page = request.GET.get('page')
    transactions_page = paginator.get_page(page)
    
    return render(request, 'blood_inventory/history.html', {
        'transactions': transactions_page,
        'query': query
    })

def low_stock_alerts(request):
    low_stock = BloodStock.objects.filter(
        quantity__lte=F('low_stock_threshold'),
        quantity__gt=0
    ).order_by('quantity')
    
    critical_stock = BloodStock.objects.filter(quantity=0)
    
    context = {
        'low_stock_alerts': low_stock,
        'critical_alerts': critical_stock,
    }
    return render(request, 'blood_inventory/low_stock_alerts.html', context)