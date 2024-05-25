from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def create_bills(request):
    return render(request, 'Management/CreateBills.html')


     
