from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from Management.models import Notification
from Tenant.models import MaintenenceRequest, VisitorRegistrationTenant
from Security.models import VisitorRegistration
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout

def main(request):
    return render(request,'Main/main.html',)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid login credentials.")
    return render(request, 'Main/login.html')

def singup_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Userinfo.objects.filter(username=username).exists():
            messages.error(request, "Username already Exists")
        else:
            userinfo = Userinfo(username=username,password=password)
            userinfo.save()
        messages.success(request, 'User Created successfully!')
        return redirect('main')
    return render(request, 'Main/singup.html',)

def logout_page(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('main')

def dashboard(request):
    visitorlog = VisitorRegistration.objects.all().order_by('-datetime_local')
    maintenance_requests = MaintenenceRequest.objects.all()
    total_maintenance_requests = maintenance_requests.count()
    total_visitors = visitorlog.count()
    last_visitor = visitorlog.first() if total_visitors > 0 else None
    visitorlogs = VisitorRegistrationTenant.objects.all().order_by('-datetime_local')
    notifications = Notification.objects.all().order_by('-post_date').first()
  

    context = {
        "total_visitors":total_visitors,
        "last_visitor": last_visitor,
        "maintenance_requests": maintenance_requests,
        "total_maintenance_requests": total_maintenance_requests,
        "visitorlogs": visitorlogs,
        "notifications": notifications,
    }

    return render(request,'Main/Dashboard.html',context)