from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *



def dashboard_security(request):
    return render(request, 'Security/DashboardSecurity.html')


def visitor_log(request):
    return render(request, 'Security/VisitorLog.html')

def incident_reporting(request):
    return render(request, 'Security/IncidentRep.html')

def patrol_reporting(request):
    return render(request, 'Security/PatrolRep.html')

def qr(request):
    return render(request, 'Security/Qr.html',)
     
def visitor_registration(request):
    if request.method == "POST":
        name = request.POST.get('full_name')
        tenant_name = request.POST.get('tenant_name')
        floor_number = request.POST.get('floor_number')
        unit_number = request.POST.get('unit_number')
        phone_number = request.POST.get('phone_number')
        home_address = request.POST.get('home_address')
        reason_to_visit = request.POST.get('reason_to_visit')
        tower_select = request.POST.get('tower_select')
        datetime_local = request.POST.get('datetime_local')

        Registration = VisitorRegistration(
            name=name,
            tenant_name=tenant_name,
            floor_number=floor_number,
            unit_number=unit_number,
            phone_number=phone_number,
            home_address=home_address,
            reason_to_visit=reason_to_visit,
            tower_select=tower_select,
            datetime_local=datetime_local,
        )
        Registration.save()
        messages.success(request,'Visitor Register successfully!')
        return redirect('visitorregistration')
    return render(request, 'Security/VisitorReg.html')

def visitor_log(request):
    visitorlog = VisitorRegistration.objects.all()
    context = {
        'visitorlog':visitorlog
    }   
    return render(request, 'Security/VisitorLog.html',context)

def delete_visitor(request, id):
    delvisitor = VisitorRegistration.objects.get(pk=id)
    delvisitor.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('visitorlog')

# def update_history(request, id):
#     if request.method == "POST":
#         name = request.POST.get('full_name')
#         floor_number = request.POST.get('floor_number')
#         unit_number = request.POST.get('unit_number')
#         facility = request.POST.get('facility')
#         booking_date = request.POST.get('date')
#         booking_time = request.POST.get('time')
#         num_attendees = request.POST.get('attendees')
#         additional_notes = request.POST.get('additional_notes')
#         edit = FacilityBooking.objects.get(pk=id)
#         edit.booker_name = name
#         edit.floor_number = floor_number
#         edit.unit_number = unit_number
#         edit.facility = facility
#         edit.booking_date = booking_date
#         edit.booking_time = booking_time
#         edit.attendees = num_attendees
#         edit.additional_notes = additional_notes
#         edit.save()
#         messages.success(request, 'Updated successfully')
#         return redirect('bookinghistory')
#     booking_history = FacilityBooking.objects.get(pk=id)
#     context = {
#         'booking_history':booking_history
#     }   
#     return render(request, 'Tenant/EditHistory.html', context)