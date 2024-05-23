from django.contrib import messages
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


def available_facilities(request):
    return render(request, 'Tenant/AvailableFacilities.html')

def booking_history(request):
    return render(request, 'Tenant/BookingHistory.html')

from django.shortcuts import render, redirect
from .models import FacilityBooking

def book_facilities(request):
    if request.method == "POST":
        name = request.POST.get('full_name')
        floor_number = request.POST.get('floor_number')
        unit_number = request.POST.get('unit_number')
        facility = request.POST.get('facility')
        booking_date = request.POST.get('date')
        booking_time = request.POST.get('time')
        num_attendees = request.POST.get('attendees')
        additional_notes = request.POST.get('addtional_notes')

        # Create a new FacilityBooking instance
        booking = FacilityBooking(
            booker_name=name,
            floor_number=floor_number,
            unit_number=unit_number,
            facility=facility,
            booking_date=booking_date,
            booking_time=booking_time,
            attendees=num_attendees,
            additional_notes=additional_notes
        )
        booking.save()
        messages.success(request, 'Facility booking is successful!')
        return redirect('bookfacilities')
    return render(request, 'Tenant/BookFacilities.html')

def booking_history(request):
    booking_history = FacilityBooking.objects.all()    
    return render(request, 'Tenant/BookingHistory.html',{'booking_history':booking_history})

def delete_history(request, id):
    dele = FacilityBooking.objects.get(pk=id)
    dele.delete()
    messages.success(request, 'Tenant deleted successfully')
    return redirect('bookinghistory')