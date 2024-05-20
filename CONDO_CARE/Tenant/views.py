from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *

def maintenenece_request(request):
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
       addTenant1 = MaintenenceRequest(full_name=full_name,email=email,phone_number=phone_number, occupation=occupation, nationality=nationality,date_of_birth=date_of_birth,  passport_or_nric=passport_or_nric,driving_license=driving_license,home_address=home_address)
       addTenant1.save()
       return redirect('maintenenecerequest')
    return render(request, 'Tenant/MainReq.html')
def request_history(request):
    return render(request, 'Tenant/RequestHistory.html')
