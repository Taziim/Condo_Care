from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Management.models import Announcement, Facility
from .models import *


def dashboard_tenant(request):
    return render(request, 'Tenant/DashboardTenant.html')

def maintenenece_request(request):
    if request.method == "POST":         
        name = request.POST.get("Tenant")
        issue_type = request.POST.get("issue_type")
        location = request.POST.get("location")
        request_datetime = request.POST.get("request_datetime")
        priority = request.POST.get("priority")
        description = request.POST.get("description")
        
        maintenenecerequest = MaintenenceRequest(
            name=name, 
            issue_type=issue_type, 
            location=location, 
            request_datetime=request_datetime, 
            priority=priority,
            description=description,
        )
        
        if 'photo' in request.FILES:
            maintenenecerequest.photo = request.FILES['photo']
        
        maintenenecerequest.save()
        return redirect('tenant:maintenenecerequest')  
    return render(request, 'Tenant/MainReq.html')

def request_history(request):
    requesthistory = MaintenenceRequest.objects.all()    
    return render(request, 'Tenant/RequestHistory.html',{'request_history':requesthistory})

def available_facilities(request):
    return render(request, 'Tenant/AvailableFacilities.html')

def booking_history(request):
    return render(request, 'Tenant/BookingHistory.html')

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
        return redirect('tenant:bookfacilities')
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
        return redirect('tenant:bookinghistory')
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

        complaint = MakeComplaint(
            name=name,
            floor_number=floor_number,
            unit_number=unit_number,
            category=category,
            date=date,
            description=description,
        )
        
        if 'attachment' in request.FILES:
            complaint.attachment = request.FILES['attachment']

        complaint.save()
        messages.success(request, 'Complaint submitted successfully!')
        return redirect('tenant:complainhistory')
        
    return render(request, 'Tenant/MakeComplain.html')
 
def delete_complain_history(request, id):
    delhistory = MakeComplaint.objects.get(pk=id)
    delhistory.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('complainhistory')

def outstanding_bills(request):
    return render(request, 'Tenant/OutstandingBill.html')

def create_visitor(request):
    if request.method == 'POST':
        visitor = VisitorRegistrationTenant(
            visitor_name=request.POST['visitor_name'],
            visitor_contact=request.POST['visitor_contact'],
            floor_number=request.POST['floor_number'],
            unit_number=request.POST['unit_number'],
            reason_to_visit=request.POST['reason_to_visit'],
            datetime_local=request.POST['datetime_local']
        )
        visitor.save()
        messages.success(request, 'Visitor registered successfully!')
        return redirect('tenant:createvisitor')
    return render(request, 'Tenant/CreateVisitor.html')

def make_payment(request):
    if request.method == "POST":
        payment_month = request.POST.get('payment_month')
        rent_amount = request.POST.get('rent_amount')
        electricity_amount = request.POST.get('electricity_amount')
        water_amount = request.POST.get('water_amount')
        payment_method = request.POST.get('payment_method')
        proof_of_rent = request.FILES.get('proof_of_rent')
        proof_of_electricity = request.FILES.get('proof_of_electricity')
        proof_of_water = request.FILES.get('proof_of_water')

        payment = TenantPayment(
            payment_month=payment_month,
            rent_amount=rent_amount,
            electricity_amount=electricity_amount,
            water_amount=water_amount,
            payment_method=payment_method,
            proof_of_rent=proof_of_rent,
            proof_of_electricity=proof_of_electricity,
            proof_of_water=proof_of_water
        )
        payment.save()
        messages.success(request, 'Payment Done Successfully')
        return redirect('makepayment')
    return render(request, 'Tenant/MakePayment.html')

def delete_request(request, id):
    delhistory = MaintenenceRequest.objects.get(pk=id)
    delhistory.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('requesthistory')

def available_facilities(request):
    availablefacilities = Facility.objects.all()
    context = {
        'availablefacilities':availablefacilities
    }   
    return render(request, 'Tenant/AvailableFacilities.html',context)

def view_announcement(request):
    viewannouncements = Announcement.objects.all()
    context = {
        'viewannouncements':viewannouncements
    }   
    return render(request, 'Tenant/ViewAnnouncement.html',context)

def delete_announcement(request, id):
    deleteannouncement = Announcement.objects.get(announcement_id=id)
    deleteannouncement.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('tenant:viewannouncement')