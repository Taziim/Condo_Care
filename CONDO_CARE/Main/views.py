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

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            try:
                userinfo = Userinfo.objects.get(username=username)
                usertypes = userinfo.usertype
                if usertypes == 'Tenant':
                    return HttpResponse('tenant:dashboardtenant')
                elif usertypes == 'Owner':
                    return redirect('owner:dashboardowner')
                elif usertypes == 'Security':
                    return redirect('security:dashboardsecurity')
                elif usertypes == 'Management':
                    return redirect('management:dashboardmanagement')
                else:
                    return redirect('main')
            except Userinfo.DoesNotExist:
                messages.error(request, "User info not found.")
                return redirect('main')
        else:
            messages.error(request, "Invalid login credentials.")
    return render(request, 'Main/login.html')

def singup_page(request):
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
        return redirect('main')
    return render(request, 'Main/singup.html',)
