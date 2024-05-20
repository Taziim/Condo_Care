from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def visitor_registration(request):
    return render(request, 'Security/VisitorReg.html')
def incident_reporting(request):
    return render(request, 'Security/IncidentRep.html')
def patrol_reporting(request):
    return render(request, 'Security/PatrolRep.html')
def qr(request):
    return render(request, 'Security/Qr.html',)
     
#     name = "welcome to"
#     obj = Qrcode.objects.get(id=1)
#     context = {
#         'name': name,
#         'obj': obj,
#     }
     
