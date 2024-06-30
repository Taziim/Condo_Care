from django.http import HttpResponse, HttpResponseRedirect
from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login

def main(request):
    return render(request,'Main/main.html',)

def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            try:
                # Get the Userinfo object for this user
                userinfo = Userinfo.objects.get(username=username)
                usertype = userinfo.usertype  # Get the usertype

                if usertype == 'Tenant':
                    return redirect('tenant:dashboardtenant')
                elif usertype == 'Owner':
                    return redirect('owner:dashboard_owner')
                elif usertype == 'Security':
                    return redirect('security:dashboard_security')
                elif usertype == 'Management':
                    return redirect('management:dashboard_management')
                else:
                    return redirect('main')
            except Userinfo.DoesNotExist:
                messages.error(request, "User info not found.")
                return redirect('main')
        else:
            messages.error(request, "Invalid login credentials.")
    return render(request, 'Main/login.html')

def sing_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        usertype = request.POST.get('usertype')
        password = request.POST.get('password')

        if Userinfo.objects.filter(username=username).exists():
            messages.error(request, "Username already Exists")
        else:
            userinfo = Userinfo(username=username, usertype=usertype, password=password)
            userinfo.password = make_password(password)
            userinfo.save()
        messages.success(request, 'User Created successfully!')
    return render(request, 'Main/singup.html',)