from django.http import FileResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Tenant.models import TenantPayment
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.conf import settings
import os

def dashboard_owner(request):
    return render(request, 'Owner/DashboardOwner.html')

def create_notification_Owner(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_date = request.POST.get('post_date')
        audience = request.POST.get('audience')

        createnotificationowner = NotificationOwner(
            title=title,
            content=content,
            post_date=post_date,
            audience=audience,
        )
        createnotificationowner.save()
        messages.success(request,'Notification Created successfully!')
        return redirect('owner:createnotificationowner')
    return render(request, 'Owner/CreateNotificationOwner.html')

def notification_log_Owner(request):
    notificationlogowner = NotificationOwner.objects.all()
    context = {
        'notificationlogowner':notificationlogowner
    }   
    return render(request, 'Owner/NotificationLog.html',context)

def delete_notification_Owner(request, id):
    deletenotificationowner = NotificationOwner.objects.get(notification_id=id)
    deletenotificationowner.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('owner:notificationlogowner')

def edit_notification_Owner(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_date = request.POST.get('post_date')
        audience = request.POST.get('audience')
    
        notificationowner = NotificationOwner.objects.get(notification_id=id)
        notificationowner.title = title
        notificationowner.content = content
        notificationowner.post_date = post_date
        notificationowner.audience = audience
        
        notificationowner.save()
        messages.success(request, 'Updated Notification successfully')
        return redirect('owner:notificationlogowner')
    update_notification_owner = NotificationOwner.objects.get(notification_id=id)
    context = {
        'update_notification_owner': update_notification_owner
    }
    return render(request, 'Owner/EditNotificationOwner.html.', context)

def create_announcement_owner(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_date = request.POST.get('post_date')

        createannouncementowner = AnnouncementOwner(
            title=title,
            content=content,
            post_date=post_date,
        )
        createannouncementowner.save()
        messages.success(request,'Announcement Created successfully!')
        return redirect('owner:createannouncementowner')
    return render(request, 'Owner/CreateAnnouncementOwner.html')

def announcement_log_owner(request):
    announcementlogowner = AnnouncementOwner.objects.all()
    context = {
        'announcementlogowner':announcementlogowner
    }   
    return render(request, 'Owner/AnnouncementLog.html',context)

def delete_announcement_log(request, id):
    deleteannouncementlogowner = AnnouncementOwner.objects.get(announcement_id=id)
    deleteannouncementlogowner.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('owner:announcementlogowner')

def update_announcement_owner(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post_date = request.POST.get('post_date')
    
        announcementowner = AnnouncementOwner.objects.get(announcement_id=id)
        announcementowner.title = title
        announcementowner.content = content
        announcementowner.post_date = post_date
        announcementowner.save()
        messages.success(request, 'Updated Announcement successfully')
        return redirect('owner:announcementlogowner')
    updateannouncementowner = AnnouncementOwner.objects.get(announcement_id=id)
    context = {
        'updateannouncementowner': updateannouncementowner
    }
    return render(request, 'Owner/EditAnnouncementOwner.html', context)

def download_pdf(request, pdf_id):
    pdf_file = TenantPayment.objects.get(pk=pdf_id).proof_of_rent
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="proof_of_rent.pdf"'
    return response

def add_tenant1(request,):
    if request.method == "POST":
       full_name = request.POST.get('full_name')
       email = request.POST.get('email')
       phone_number = request.POST.get('phone_number')
       occupation = request.POST.get('occupation')
       date_of_birth = request.POST.get('date_of_birth')
       nationality = request.POST.get('nationality')
       home_address = request.POST.get('home_address')
       passport_or_nric = request.FILES['passport_or_nric']
       driving_license = request.FILES['driving_license']
       addTenant1 = Addform1(full_name=full_name,email=email,phone_number=phone_number, occupation=occupation, nationality=nationality,date_of_birth=date_of_birth,  passport_or_nric=passport_or_nric,driving_license=driving_license,home_address=home_address)
       addTenant1.save()
       return redirect('owner:addtenant2')
    return render(request, 'owner/addTenantown1.html',)

def add_tenant2(request):
    if request.method == "POST":
        fitness_center = request.POST.get('fitness_center') == 'on'
        swimming_pool = request.POST.get('swimming_pool') == 'on'
        parking_facilities = request.POST.get('parking_facilities') == 'on'
        children_play_area = request.POST.get('children_play_area') == 'on'
        clubhouse = request.POST.get('clubhouse') == 'on'
        playground = request.POST.get('playground') == 'on'

        addAmenities = Addform2(
            fitness_center=fitness_center,
            swimming_pool=swimming_pool,
            parking_facilities=parking_facilities,
            children_play_area=children_play_area,
            clubhouse=clubhouse,
            playground=playground
        )
        addAmenities.save()
        return redirect('owner:addtenant3') 
    return render(request, 'owner/addTenantown2.html')

def add_tenant3(request):
    if request.method == "POST":
        Contract_term = request.POST.get('Contract_term')
        floor_number = request.POST.get('floor_number')
        unit_number = request.POST.get('unit_number')
        security_deposit = request.POST.get('security_deposit')
        refundable_amount = request.POST.get('refundable_amount') 
        rent_fee = request.POST.get('rent_fee')
        rent_date = request.POST.get('rent_date')
        additional_charges = request.POST.get('additional_charges') 
        parking_slot = request.POST.get('parking_slot') 
        tenant_insurance = request.POST.get('tenant_insurance')

        addContract = Addform3(
            Contract_term=Contract_term,
            floor_number=floor_number,
            unit_number=unit_number,
            security_deposit=security_deposit,
            refundable_amount=refundable_amount,
            rent_fee=rent_fee,
            rent_date=rent_date,
            additional_charges=additional_charges,
            parking_slot=parking_slot,
            tenant_insurance=tenant_insurance

            )
        addContract.save()
        return redirect('owner:dashboardowner')  
    return render(request, 'Owner/addTenantown3.html')

def view_tenant_info(request):
    tenantinfo = Addform1.objects.all()
    context = {
        'tenantinfo':tenantinfo
    }
    return render(request, 'Owner/ViewTenantInfo.html',context)

def view_tenant_agree(request):
    viewagreements = Addform3.objects.all()
    amenities = Addform1.objects.values('full_name')
    context = {
        'viewagreements': viewagreements,
        'amenities': amenities,
    }   
    return render(request, 'Owner/ViewTenantAgree.html', context)

def delete_info(request, id):
    delete_info = Addform1.objects.get(id=id)
    delete_info.delete()
    messages.success(request, 'Tenant deleted successfully')
    return redirect('owner:viewtenantinfo')

def delete_agree(request, id):
    delete_agree = Addform3.objects.get(id=id)
    delete_agree.delete()
    messages.success(request, 'Tenant deleted successfully')
    return redirect('owner:viewtenantagree')

def download_passport_or_nric(request, id):
    addform1 = Addform1.objects.get(id=id).passport_or_nric
    response = HttpResponse(addform1, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="passport_or_nric.pdf"'
    return response

def download_driving_license(request, id):
    addform1 = Addform1.objects.get(id=id).driving_license
    response = HttpResponse(addform1, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="driving_license.pdf"'
    return response


