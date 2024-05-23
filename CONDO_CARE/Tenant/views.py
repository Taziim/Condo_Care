from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *

def maintenenece_request(request):
    if request.method == "POST":         
        name = request.POST.get("Tenant",'')
        issue_type = request.POST.get("issue_type",'')
        location = request.POST.get("location",'')
        request_datetime = request.POST.get("request_datetime",'')
        priority = request.POST.get("priority",'')
        photo = request.POST.get("photo",'')
        maintenenecerequest = MaintenenceRequest(name=name, issue_type=issue_type, location=location, request_datetime=request_datetime, priority=priority, photo=photo)
        maintenenecerequest.save()
        return redirect('maintenenecerequest')  
    return render(request, 'Tenant/MainReq.html')

def request_history(request):
    requesthistory = MaintenenceRequest.objects.all()    
    return render(request, 'Tenant/RequestHistory.html',{'request_history':requesthistory})

def book_facilities(request):
    return render(request, 'Tenant/BookFacilities.html')

def available_facilities(request):
    return render(request, 'Tenant/AvailableFacilities.html')

def booking_history(request):
    return render(request, 'Tenant/BookingHistory.html')
