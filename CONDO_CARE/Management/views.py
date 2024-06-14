from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def create_bills(request):
    return render(request, 'Management/CreateBills.html')

def dashboard_management(request):
    return render(request, 'Management/DashboardManagement.html')

def notification_announcement(request):
    return render(request, 'Management/Notifications.html')


     
