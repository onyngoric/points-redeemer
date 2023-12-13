from django.db import models
from django.utils import timezone

# Create your models here.
class Customers (models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, primary_key=True)
    added_on = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Customers"
    def __str__(self):
        return self.full_name
        
    
class Payments (models.Model):
    phone = models.ForeignKey(Customers, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    paid_on = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Payments"
    def __str__(self):
        return self.phone

class Points (models.Model):
    phone = models.ForeignKey(Customers, on_delete=models.PROTECT)
    points = models.IntegerField(default=0)
    redeemed = models.IntegerField(default=0)
    redeemed_on = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Points"
    def __str__(self):
        return self.phone