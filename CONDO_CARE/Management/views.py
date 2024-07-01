from django.http import FileResponse, Http404, HttpResponse
from Tenant.models import FacilityBooking, MaintenenceRequest, MakeComplaint
from .models import *
from django.contrib import messages
from django.shortcuts import redirect, render

def dashboard_management(request):
    return render(request, 'Management/DashboardManagement.html')


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
        return redirect('management:createannouncement')
    return render(request, 'Management/CreateAnnouncement.html')

def announcement_log(request):
    announcementlog = Announcement.objects.all()
    context = {
        'announcementlog':announcementlog
    }   
    return render(request, 'Management/AnnouncementLog.html',context)

def delete_announcement_log(request, id):
    deleteannouncementlog = Announcement.objects.get(announcement_id=id)
    deleteannouncementlog.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('management:announcementlog')
    
def edit_announcement(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_date = request.POST.get('post_date')
    
        announcement = Announcement.objects.get(announcement_id=id)
        announcement.title = title
        announcement.content = content
        announcement.post_date = post_date
        announcement.save()
        messages.success(request, 'Updated Announcement successfully')
        return redirect('management:announcementlog')
    update_announcement = Announcement.objects.get(announcement_id=id)
    context = {
        'update_announcement': update_announcement
    }
    return render(request, 'Management/EditAnnouncement.html', context)

def create_notification(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_date = request.POST.get('post_date')
        audience = request.POST.get('audience')

        createnotification = Notification(
            title=title,
            content=content,
            post_date=post_date,
            audience=audience,
        )
        createnotification.save()
        messages.success(request,'Notification Created successfully!')
        return redirect('management:createnotification')
    return render(request, 'Management/CreateNotification.html')

def notification_log(request):
    notificationlog = Notification.objects.all()
    context = {
        'notificationlog':notificationlog
    }   
    return render(request, 'Management/NotificationLog.html',context)

def delete_notification_log(request, notification_id):
    deletenotificationlog = Notification.objects.get(notification_id=notification_id)
    deletenotificationlog.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('management:notificationlog')
    
def edit_notification(request, notification_id):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_date = request.POST.get('post_date')
        audience = request.POST.get('audience')
    
        notification = Notification.objects.get(notification_id=notification_id)
        notification.title = title
        notification.content = content
        notification.post_date = post_date
        notification.audience = audience
        
        notification.save()
        messages.success(request, 'Updated Notification successfully')
        return redirect('management:notificationlog')
    update_notification = Notification.objects.get(notification_id=notification_id)
    context = {
        'update_notification': update_notification
    }
    return render(request, 'Management/EditNotifications.html', context)

def maintenance_request_management(request):
    maintenancerequestmanagement = MaintenenceRequest.objects.all()
    context = {
        'maintenancerequestmanagement':maintenancerequestmanagement
    }   
    return render(request, 'Management/RequestHistoryManagement.html',context)

def delete_maintenance_request(request, id):
    deletemaintenancerequest = MaintenenceRequest.objects.get(id=id)
    deletemaintenancerequest.delete()
    messages.success(request, 'Deleted Maintenence Request successfully')
    return redirect('management:maintenancerequestmanagement')

def update_maintenance_request(request, id):
    updatemaintenancerequest = MaintenenceRequest.objects.get(pk=id)
    if request.method == "POST":
        status = request.POST.get('status')
        updatemaintenancerequest.status = status
        updatemaintenancerequest.save()
        messages.success(request, 'Updated Maintenence Request successfully')
        return redirect('management:maintenancerequestmanagement')
    
    context = {
        'updatemaintenancerequest': updatemaintenancerequest,
        'STATUS_CHOICES': MaintenenceRequest.STATUS_CHOICES
    }
    return render(request, 'Management/UpdateMaintenence.html', context)

def download_image_maintence(request, id):
    downloadimagemaintence = MaintenenceRequest.objects.get(pk=id)
    if downloadimagemaintence.photo:
        response = FileResponse(downloadimagemaintence.photo.open(), content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename="{downloadimagemaintence.photo.name}"'
        return response
    else:
        raise Http404("No image found.")
    
def tenant_booking_list(request):
    tenantbookinglist = FacilityBooking.objects.all()
    context = {
        'tenantbookinglist':tenantbookinglist
    }   
    return render(request, 'Management/BookingList.html',context)

def delete_tenant_booking(request, id):
    deletetenantbooking = FacilityBooking.objects.get(pk=id)
    deletetenantbooking.delete()
    messages.success(request, 'Deleted Tenant Booking successfully')
    return redirect('management:tenantbookinglist')

def manage_facilities(request):
    if request.method == 'POST':
        facilities_data = [
            {
                'name': 'Common Room',
                'available': request.POST.get('common_room_available') == 'yes',
                'capacity': request.POST.get('common_room_capacity'),
                'available_time': request.POST.get('common_room_time')
            },
            {
                'name': 'Hall Room',
                'available': request.POST.get('hall_room_available') == 'yes',
                'capacity': request.POST.get('hall_room_capacity'),
                'available_time': request.POST.get('hall_room_time')
            },
            {
                'name': 'Swimming Pool',
                'available': request.POST.get('swimming_pool_available') == 'yes',
                'capacity': request.POST.get('swimming_pool_capacity'),
                'available_time': request.POST.get('swimming_pool_time')
            },
            {
                'name': 'BBQ Area',
                'available': request.POST.get('bbq_area_available') == 'yes',
                'capacity': request.POST.get('bbq_area_capacity'),
                'available_time': request.POST.get('bbq_area_time')
            },
            {
                'name': 'Rooftop Terrace',
                'available': request.POST.get('rooftop_terrace_available') == 'yes',
                'capacity': request.POST.get('rooftop_terrace_capacity'),
                'available_time': request.POST.get('rooftop_terrace_time')
            },
            {
                'name': 'Sports Facilities',
                'available': request.POST.get('sports_facilities_available') == 'yes',
                'capacity': request.POST.get('sports_facilities_capacity'),
                'available_time': request.POST.get('sports_facilities_time')
            }
        ]

        for data in facilities_data:
            Facility.objects.update_or_create(
                name=data['name'],
                defaults={
                    'available': data['available'],
                    'capacity': data['capacity'],
                    'available_time': data['available_time']
                }
            )
        messages.success(request, 'Added Facilities successfully')
        return redirect('management:managefacilities')
    return render(request, 'Management/ManageFacilities.html')

def view_facilities(request):
    view_facilities = Facility.objects.all()
    context = {
        'view_facilities':view_facilities
    }   
    return render(request, 'Management/EditFacilities.html',context)

def delete_all_facilities(request):
    if request.method == 'POST':
        Facility.objects.all().delete()
        return redirect('management:viewfacilities')  

    return render(request, 'Management/Deletefacilities.html')

def complain_history_tenant(request):
    complainhistorytenant = MakeComplaint.objects.all()
    context = {
        'complainhistorytenant':complainhistorytenant
    }   
    return render(request, 'Management/ComplainTenant.html',context)

def delete_history_tenant(request, id):
    deletehistorytenant = MakeComplaint.objects.get(id=id)
    deletehistorytenant.delete()
    messages.success(request, 'Deleted Tenant history successfully')
    return redirect('management:complainhistorytenant')

    
def download_image_complainhistory(request, id):
    downloadimagecomplainhistory = MakeComplaint.objects.get(id=id)
    if downloadimagecomplainhistory.attachment:
        response = FileResponse(downloadimagecomplainhistory.attachment.open(), content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename="{downloadimagecomplainhistory.attachment.name}"'
        return response
    else:
        raise Http404("No image found.")    
