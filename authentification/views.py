from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# User model = table

def register(request):
    if request.user.is_authenticated:
        return redirect('index.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        sex = request.POST.get('sex')
        address = request.POST.get('address')
        password = request.POST.get('email')
        confirm = request.POST.get('confirm')


        
    if confirm != password:
        messages.error(request, 'confirmation invalid')
    elif User.objects.filter(username=username).exists():
        messages.error(request,'username invalid')
    else:
        User.objects.create_user(username=username , email=email, phone= phone, sex=sex, address=address ,password=password)
        return redirect('login')
    

    return render(request , 'auth/register.html')