from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import Customer

# User model = table

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        contact = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        sex = request.POST['sex']

        if password != confirm_password:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d’utilisateur existe déjà.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        Customer.objects.create(
            user=user,
            address=address,
            phone=contact,
            city=city,
            sex=sex,
            role='client'  # client par défaut
        )

        messages.success(request, 'Inscription réussie. Connectez-vous maintenant.')
        return redirect('login')

    return render(request, 'auth/register.html')

def login_view(request):
    if request.user.is_authenticated: # mi-retourne boolean
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')
            return redirect('login')

    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')