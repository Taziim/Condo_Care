from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import FileResponse, HttpResponseNotFound
from django.http import FileResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .models import Userinfo

def main(request):
    return render(request,'Main/main.html',)
def log_in(request):
        if request.method == "POST":
             username = request.POST.get('username')
             password = request.POST.get('password')
             user = authenticate(request, username=username,password=password)
             if user is not None:
               login(request,user)
               return redirect('signup')
             else:
                 return HttpResponse("Invalid login credentials")
        return render(request,'Main/login.html');

# def delete(request, id):
#     dele = Addform1.objects.get(id=id)
#     dele.delete()
#     messages.success(request, 'Tenant deleted successfully!')
#     return redirect('viewTenant')

def sing_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        user_type = request.POST.get('userType')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        userinfo = Userinfo(username=username, user_type=user_type, password=password)
        userinfo.save()
        messages.success(request, 'User Created successfully!')
    return render(request, 'Main/singup.html',)
