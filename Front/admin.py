from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customers)
admin.site.register(Payments) #remember to deregister
admin.site.register(Points) #remember to deregister