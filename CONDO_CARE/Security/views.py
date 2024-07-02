from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Tenant.models import VisitorRegistrationTenant
from .models import *



def view_visitor(request):
    return render(request, 'Security/ViewVisitor.html')

def dashboard_security(request):
    return render(request, 'Security/DashboardSecurity.html')


def incident_reporting(request):
    if request.method == "POST":
        incidenttype = request.POST.get('incidenttype')
        description = request.POST.get('description')
        location = request.POST.get('location')
        datetimereported = request.POST.get('datetimereported')


        incidentreporting = IncidentReport(
            incidenttype=incidenttype,
            description=description,
            location=location,
            datetimereported=datetimereported,

        )
        if 'photo' in request.FILES:
            incidentreporting.photo = request.FILES['photo']

        incidentreporting.save()
        messages.success(request,'Incident Register successfully!')
        return redirect('security:incidentreporting')
    return render(request, 'Security/IncidentRep.html')


def patrol_reporting(request):
    return render(request, 'Security/PatrolRep.html')
     
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
        return redirect('security:visitorregistration')
    return render(request, 'Security/VisitorReg.html')

def visitor_log(request):
    visitorlog = VisitorRegistration.objects.all()
    context = {
        'visitorlog':visitorlog
    }   
    return render(request, 'Security/VisitorLog.html',context)

def delete_visitor(request, id):
    delvisitor = VisitorRegistration.objects.get(id=id)
    delvisitor.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('security:visitorlog')

def update_visitor(request, id):
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
        visitor = VisitorRegistration.objects.get(id=id)
        visitor.name = name
        visitor.tenant_name = tenant_name
        visitor.floor_number = floor_number
        visitor.unit_number = unit_number
        visitor.phone_number = phone_number
        visitor.home_address = home_address
        visitor.reason_to_visit = reason_to_visit
        visitor.tower_select = tower_select
        visitor.datetime_local = datetime_local
        visitor.save()
        messages.success(request, 'Updated successfully')
        return redirect('security:visitorlog')
    update_visitor = VisitorRegistration.objects.get(id=id)
    context = {
        'update_visitor': update_visitor
    }
    return render(request, 'Security/EditVisitor.html', context)


def security_emergency(request):
    return render(request, 'Security/Emergency.html',)

def view_visitor(request):
    viewvisitor = VisitorRegistrationTenant.objects.all()
    context = {
        'viewvisitor':viewvisitor
    }   
    return render(request, 'Security/ViewVisitor.html',context)

def delete_visitor_tenant(request, id):
    deletevisitor = VisitorRegistrationTenant.objects.get(pk=id)
    deletevisitor.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('security:viewvisitor')

