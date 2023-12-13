from django.shortcuts import render
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    customers = Customers.objects.prefetch_related('payments_set','points_set').all()
    return render(request, 'home.html',{'customers':customers})

def pay(request):
    return render(request, 'pay.html')

def points(request):
    return render(request, 'points.html')
    
def pointsSearch(request):
   if request.method == 'POST':        
        checkphone=request.POST.get('phoneSearch')
        getCustomer = Customers.objects.filter(phone=checkphone)
        if getCustomer:                             
            return render (request, 'points.html', {'customers':getCustomer})                
        else:
            messages.error(request,'User not found')
            return render(request, 'points.html')

def redeem(request):
    if request.method == 'POST':
        checkphone = request.POST.get('pk')
        toRedeem =int(request.POST.get('points'))
        availablePnts = int(Points.objects.filter(phone=checkphone).values_list('points', flat=True)[0])#changing query set to int
        redeemedPnts = int(Points.objects.filter(phone=checkphone).values_list('redeemed',flat=True)[0])#changing query set to int
        Points.objects.filter(phone=checkphone).update(points=availablePnts-toRedeem,redeemed=redeemedPnts+toRedeem)
        newDetails = Customers.objects.filter(phone=checkphone)
        messages.success(request, 'Points redeemed successfully')
        return render (request, 'points.html', {'customers':newDetails})
    
def paySearch(request):
    if request.method == 'POST':        
        checkphone=request.POST.get('phoneSearch')
        getCustomer = Customers.objects.filter(phone=checkphone)
        if getCustomer:                             
            return render (request, 'pay.html', {'customers':getCustomer})                
        else:
            messages.error(request,'User not found')
            return render(request, 'pay.html')
        
def awardPoints(request):
    if request.method == 'POST':
        checkphone = request.POST.get('pk')
        amount = int(request.POST.get('amount'))
        if Points.objects.filter(phone=checkphone).exists() == True:
            availablePnts = int(Points.objects.filter(phone=checkphone).values_list('points', flat=True)[0])
            availableAmnt = int(Payments.objects.filter(phone=checkphone).values_list('amount', flat=True)[0])
            pointsAwarded = (5/100)*amount
            Payments.objects.filter(phone=checkphone).update(amount=availableAmnt+amount)
            Points.objects.filter(phone=checkphone).update(points=availablePnts+pointsAwarded)
            messages.success(request, 'Payment Recieved')
            return render (request, 'pay.html')
