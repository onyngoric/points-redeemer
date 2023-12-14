from django.db import models
from django.utils import timezone

# Create your models here.
class Customers (models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, primary_key=True)
    amount = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    redeemed = models.IntegerField(default=0)
    changed_on = models.DateTimeField(default=timezone.now)


    
    class Meta:
        verbose_name_plural = "Customers"
    def __str__(self):
        return self.phone