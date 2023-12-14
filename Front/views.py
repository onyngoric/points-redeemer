from django.shortcuts import render
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    customers = Customers.objects.all()
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
            messages.error(request,'Customer not found')
            return render(request, 'points.html')

def redeem(request):
    if request.method == 'POST':
        checkphone = request.POST.get('pk')
        toRedeem =int(request.POST.get('points'))
        availablePnts = int(Customers.objects.filter(phone=checkphone).values_list('points', flat=True)[0])#changing query set to int
        redeemedPnts = int(Customers.objects.filter(phone=checkphone).values_list('redeemed',flat=True)[0])#changing query set to int
        Customers.objects.filter(phone=checkphone).update(points=availablePnts-toRedeem,redeemed=redeemedPnts+toRedeem)
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
        if Customers.objects.filter(phone=checkphone).exists() == True:
            availablePnts = int(Customers.objects.filter(phone=checkphone).values_list('points', flat=True)[0])
            availableAmnt = int(Customers.objects.filter(phone=checkphone).values_list('amount', flat=True)[0])
            pointsAwarded = (5/100)*amount
            Customers.objects.filter(phone=checkphone).update(amount=availableAmnt+amount)
            Customers.objects.filter(phone=checkphone).update(points=availablePnts+pointsAwarded)
            messages.success(request, 'Payment Recieved')
            return render (request, 'pay.html')

def newUser(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        phone =request.POST.get('phone')
        amount =int(request.POST.get('amount'))
        Customers.objects.create(full_name=username,phone=phone)
        Customers.objects.filter(phone=phone).update(amount=amount)
        pointsAwarded = (5/100)*amount
        Customers.objects.filter(phone=phone).update(points=pointsAwarded,redeemed=0)
        messages.success(request, 'User Created')
        return render (request, 'new-user.html')
    else:
        return render (request, 'new-user.html')