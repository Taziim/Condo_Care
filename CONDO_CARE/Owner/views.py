from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponseNotFound
from django.http import FileResponse
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



def view_payment(request):
    makepayment = TenantPayment.objects.all()
    context = {
        'makepayment':makepayment
    }   
    return render(request, 'Owner/ViewPayment.html',context)


def download_pdf(request, pdf_id):
    pdf_file = TenantPayment.objects.get(pk=pdf_id).proof_of_rent
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="proof_of_rent.pdf"'
    return response

def delete_payment(request, pdf_id):
    deletepayment = TenantPayment.objects.get(pk=pdf_id)
    deletepayment.delete()
    messages.success(request, 'Payment deleted successfully')
    return redirect('viewpayment')









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
       return redirect('addtenant2')
    return render(request, 'owner/addTenantown1.html',)
def add_tenant2(request):
    return render(request, 'owner/addTenantown2.html',)
def add_tenant3(request):
    return render(request, 'owner/addTenantown3.html')
def view_tenant_info(request):
    tenantinfo = Addform1.objects.all()
    context = {
        'tenantinfo':tenantinfo
    }
    return render(request, 'owner/ViewTenantInfo.html',context)
def view_tenant_agree(request):
    return render(request, 'owner/ViewTenantAgree.html')

def delete(request, id):
    dele = Addform1.objects.get(id=id)
    dele.delete()
    messages.success(request, 'Tenant deleted successfully')
    return redirect('viewtenantinfo')

def download_passport_or_nric(request, id):
    addform1 = Addform1.objects.get(id=id)
    response = FileResponse(addform1.passport_or_nric)
    response['Content-Disposition'] = f'attachment; filename="{addform1.passport_or_nric.name}"'
    return response

def download_driving_license(request, id):
    addform1 = Addform1.objects.get(id=id)
    response = FileResponse(addform1.driving_license)
    response['Content-Disposition'] = f'attachment; filename="{addform1.driving_license.name}"'
    return response