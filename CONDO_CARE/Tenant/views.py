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
        booker_name = request.POST.get('full_name')
        floor_number = request.POST.get('floor_number')
        unit_number = request.POST.get('unit_number')
        facility = request.POST.get('facility')
        booking_date = request.POST.get('date')
        booking_time = request.POST.get('time')
        num_attendees = request.POST.get('attendees')
        additional_notes = request.POST.get('additional_notes')

        # Create a new FacilityBooking instance
        booking = FacilityBooking(
            booker_name=booker_name,
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
    context = {
        'booking_history':booking_history
    }   
    return render(request, 'Tenant/BookingHistory.html',context)

def delete_history(request, id):
    delhistory = FacilityBooking.objects.get(pk=id)
    delhistory.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('bookinghistory')

def update_history(request, id):
    if request.method == "POST":
        name = request.POST.get('full_name')
        floor_number = request.POST.get('floor_number')
        unit_number = request.POST.get('unit_number')
        facility = request.POST.get('facility')
        booking_date = request.POST.get('date')
        booking_time = request.POST.get('time')
        num_attendees = request.POST.get('attendees')
        additional_notes = request.POST.get('additional_notes')
        edit = FacilityBooking.objects.get(pk=id)
        edit.booker_name = name
        edit.floor_number = floor_number
        edit.unit_number = unit_number
        edit.facility = facility
        edit.booking_date = booking_date
        edit.booking_time = booking_time
        edit.attendees = num_attendees
        edit.additional_notes = additional_notes
        edit.save()
        messages.success(request, 'Updated successfully')
        return redirect('bookinghistory')
    booking_history = FacilityBooking.objects.get(pk=id)
    context = {
        'booking_history':booking_history
    }   
    return render(request, 'Tenant/EditHistory.html', context)



def complain_history(request):
    complainhistory = MakeComplaint.objects.all()
    context = {
        'complainhistory':complainhistory
    }   
    return render(request, 'Tenant/ComplainHistory.html',context)

def make_complaint(request):
    if request.method == "POST":
        name = request.POST.get('name')
        floor_number = request.POST.get('floor_number')
        unit_number = request.POST.get('unit_number')
        category = request.POST.get('category')
        date = request.POST.get('date')
        description = request.POST.get('description')
        attachment = request.FILES.get('attachment')

        # Create a new Complaint instance
        complaint = MakeComplaint(
            name=name,
            floor_number=floor_number,
            unit_number=unit_number,
            category=category,
            date=date,
            description=description,
            attachment=attachment
        )
        complaint.save()
        messages.success(request, 'Complaint submitted successfully!')
        return redirect('complainhistory')  
    return render(request, 'Tenant/MakeComplain.html')  


def delete_complain_history(request, id):
    delhistory = MakeComplaint.objects.get(pk=id)
    delhistory.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('complainhistory')

def outstanding_bills(request):
    return render(request, 'Tenant/OutstandingBill.html')

def make_payment(request):
    return render(request, 'Tenant/MakePayment.html')

def create_visitor(request):
    return render(request, 'Tenant/CreateVisitor.html')