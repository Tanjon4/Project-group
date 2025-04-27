from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# User model = table

def register(request):
    if request.user.is_authenticated:   #boolean
        return redirect('profil')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if confirm != password:
            messages.error(request, 'confirmation invalid')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'username invalid')
        else:
            User.objects.create_user(username=username , password=password)
            return redirect('login')
        

    return render(request , 'auth/register.html')

def login_view(request):
    if request.user.is_authenticated:   #boolean
        return redirect('profil')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username , password=password)

        if user:
            login(request , user) #cookie(maharitra) ou session
            return redirect('profile')
        else:
            messages.error(request,'invalid crendentials')
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    #request.user info utilisateur connecter
    return render(request, 'auth/profile.html', {'username': request.user.user})

