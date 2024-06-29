from django.http import FileResponse, Http404, HttpResponse
from Tenant.models import FacilityBooking, MaintenenceRequest
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
    

def edit_announcement(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_date = request.POST.get('post_date')
    
        announcement = Announcement.objects.get(id=id)
        announcement.title = title
        announcement.content = content
        announcement.post_date = post_date
        announcement.save()
        messages.success(request, 'Updated Announcement successfully')
        return redirect('announcementlog')
    update_announcement = Announcement.objects.get(id=id)
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
        return redirect('createnotification')
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
    return redirect('notificationlog')
    

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
        return redirect('notificationlog')
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
    return redirect('maintenancerequestmanagement')


def update_maintenance_request(request, id):
    updatemaintenancerequest = MaintenenceRequest.objects.get(pk=id)
    if request.method == "POST":
        status = request.POST.get('status')
        updatemaintenancerequest.status = status
        updatemaintenancerequest.save()
        messages.success(request, 'Updated Maintenence Request successfully')
        return redirect('maintenancerequestmanagement')
    
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
    return redirect('tenantbookinglist')



def manage_facilities(request):
    managefacilities = Facility.objects.all()
    context = {
        'managefacilities':managefacilities
    }   
    return render(request, 'Management/ManageFacilities.html',context)