from django.http import HttpResponse, HttpResponseRedirect
from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
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
            if user.usertype == 'Tenant':
                return redirect('dashboardtenant')
            # elif user.usertype == 'Owner':
            #     return redirect('dashboardowner')
            # elif user.usertype == 'Security':
            #     return redirect('dashboardsecurity')
            # elif user.usertype == 'Management':
            #     return redirect('dashboardmanagement')
            else:
                return redirect('main')  # Default redirection if user type does not match
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