from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.shortcuts import redirect, render





def create_bills(request):
    return render(request, 'Management/CreateBills.html')

def dashboard_management(request):
    return render(request, 'Management/DashboardManagement.html')

def notification_announcement(request):
    return render(request, 'Management/Notifications.html')


def create_announcement(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_date = request.POST.get('post_date')

        createannouncement = Announcement(
            title=title,
            content=content,
            post_date=post_date,
        )
        createannouncement.save()
        messages.success(request,'Announcement Created successfully!')
        return redirect('createannouncement')
    return render(request, 'Management/CreateAnnouncement.html')




def announcement_log(request):
    announcementlog = Announcement.objects.all()
    context = {
        'announcementlog':announcementlog
    }   
    return render(request, 'Management/AnnouncementLog.html',context)

def delete_announcement_log(request, id):
    deleteannouncementlog = Announcement.objects.get(id=id)
    deleteannouncementlog.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('announcementlog')
    

# def update_visitor(request, id):
#     if request.method == "POST":
#         name = request.POST.get('full_name')
#         tenant_name = request.POST.get('tenant_name')
#         floor_number = request.POST.get('floor_number')
#         unit_number = request.POST.get('unit_number')
#         phone_number = request.POST.get('phone_number')
#         home_address = request.POST.get('home_address')
#         reason_to_visit = request.POST.get('reason_to_visit')
#         tower_select = request.POST.get('tower_select')
#         datetime_local = request.POST.get('datetime_local')
#         visitor = VisitorRegistration.objects.get(id=id)
#         visitor.name = name
#         visitor.tenant_name = tenant_name
#         visitor.floor_number = floor_number
#         visitor.unit_number = unit_number
#         visitor.phone_number = phone_number
#         visitor.home_address = home_address
#         visitor.reason_to_visit = reason_to_visit
#         visitor.tower_select = tower_select
#         visitor.datetime_local = datetime_local
#         visitor.save()
#         messages.success(request, 'Updated successfully')
#         return redirect('visitorlog')
#     update_visitor = VisitorRegistration.objects.get(id=id)
#     context = {
#         'update_visitor': update_visitor
#     }
#     return render(request, 'Security/EditVisitor.html', context)


# def security_emergency(request):
#     # emergency = Emergency.objects.all()
#     # serilizers = Emergencyserializers(emergency, many = True)
#     # json_data = JSONRenderer().render(serilizers.data)
#     # return HttpResponse(json_data, content_type ='application/json')
#     return render(request, 'Security/Emergency.html',)

# # Assuming you have already imported necessary modules: VisitorRegistration, VisitorRegistrationSerializer, JSONRenderer, render

# def visitor_log(request):
#     visitor_logs = VisitorRegistration.objects.all()  # Retrieve all visitor logs from database
#     serializer = VisitorRegistrationSerializer(visitor_logs, many=True)  # Serialize the visitor logs
    
#     json_data = JSONRenderer().render(serializer.data)  # Render the serialized data into JSON format
    
#     context = {
#         # 'visitorlog': visitor_logs,  # Pass the queryset of visitor logs
#         'json_data': json_data  # Pass the JSON data to context
#     }
    
#     return render(request, 'Security/VisitorLog.html', context)
    
