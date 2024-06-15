from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework. renderers import JSONRenderer
from .models import *
from .serilizers import *



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
    delvisitor = VisitorRegistration.objects.get(id=id)
    delvisitor.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('visitorlog')

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
        return redirect('visitorlog')
    update_visitor = VisitorRegistration.objects.get(id=id)
    context = {
        'update_visitor': update_visitor
    }
    return render(request, 'Security/EditVisitor.html', context)


def security_emergency(request):
    # emergency = Emergency.objects.all()
    # serilizers = Emergencyserializers(emergency, many = True)
    # json_data = JSONRenderer().render(serilizers.data)
    # return HttpResponse(json_data, content_type ='application/json')
    return render(request, 'Security/Emergency.html',)

# Assuming you have already imported necessary modules: VisitorRegistration, VisitorRegistrationSerializer, JSONRenderer, render

# def visitor_log(request):
#     visitor_logs = VisitorRegistration.objects.all()  # Retrieve all visitor logs from database
#     serializer = VisitorRegistrationSerializer(visitor_logs, many=True)  # Serialize the visitor logs
    
#     json_data = JSONRenderer().render(serializer.data)  # Render the serialized data into JSON format
    
#     context = {
#         # 'visitorlog': visitor_logs,  # Pass the queryset of visitor logs
#         'json_data': json_data  # Pass the JSON data to context
#     }
    
#     return render(request, 'Security/VisitorLog.html', context)
