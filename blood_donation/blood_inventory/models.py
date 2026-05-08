from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

BLOOD_GROUPS = [
    ('O+', 'O+'), ('O-', 'O-'), 
    ('A+', 'A+'), ('A-', 'A-'), 
    ('B+', 'B+'), ('B-', 'B-'), 
    ('AB+', 'AB+'), ('AB-', 'AB-')
]

class BloodStock(models.Model):
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    low_stock_threshold = models.PositiveIntegerField(default=5)
    location = models.CharField(max_length=100, default="Central Blood Bank")
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['blood_group', 'location']
        ordering = ['blood_group']
    
    def __str__(self):
        return f"{self.blood_group} ({self.quantity} units)"
    
    @property
    def stock_status(self):
        if self.quantity == 0:
            return "danger"
        elif self.quantity <= self.low_stock_threshold:
            return "warning"
        return "success"
    
    @property
    def status_text(self):
        if self.quantity == 0:
            return "Out of Stock"
        elif self.quantity <= self.low_stock_threshold:
            return f"Low Stock - {self.quantity} units"
        return f"Available - {self.quantity} units"

class StockTransaction(models.Model):
    ACTION_CHOICES = [
        ('IN', 'Stock In'), ('OUT', 'Stock Out'),
        ('EXPIRE', 'Expired'), ('ADJUST', 'Adjustment')
    ]
    
    blood_stock = models.ForeignKey(BloodStock, on_delete=models.CASCADE, related_name='transactions')
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    units = models.IntegerField()
    balance_after = models.IntegerField()
    reason = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.blood_stock.blood_group} - {self.action} {self.units}"