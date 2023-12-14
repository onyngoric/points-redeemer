from django.contrib import admin
from django.urls import path
from Front import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('pay/', views.pay, name='pay'),
    path('points/', views.points, name='points'),
    path('pSearch/',views.pointsSearch, name='pSearch'),
    path('paySearch/', views.paySearch, name='paySearch'),
    path('redeem/', views.redeem, name='redeem'),
    path('award/', views.awardPoints, name='award'),
    path('new-user',views.newUser,name='new-user'),
]

admin.site.site_header = 'REMMI SPA LOYALTY POINTS Admin'
admin.site.site_title  = 'REMMI SPA LOYALTY POINTS'
admin.site.index_title   = 'Admin'
