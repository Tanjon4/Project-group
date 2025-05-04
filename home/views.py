from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
import random , os , time
from .models import Service

@login_required
def home(request):
    return render(request, 'home/index.html')

@login_required
def create_service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        images = request.FILES.get('images')
        
    
        errors = {}
        if not name:
            errors['name'] = "Le nom du service est obligatoire"
        if not description:
            errors['description'] = "La description est obligatoire"
        if not price:
            errors['price'] = "Le prix est obligatoire"
        
        if errors:
            return render(request, 'service/create_service.html', {
                'errors': errors,
                'form_data': request.POST
            })
        
    
        file_url = None
        if images:
            # Generate unique file
            unique_file_name = random.randint(100_000_000, 999_999_999)
            ext = os.path.splitext(images.name)[1] or ".jpg"
            filename = f'service-{int(time.time())}-{unique_file_name}{ext}' 
            upload_path = os.path.join(settings.BASE_DIR, 'static', 'images', filename)

            # Save file
            with open(upload_path, 'wb+') as dest:
                for chunk in images.chunks():
                    dest.write(chunk)

            file_url = f'static/images/{filename}'
        
        # Create service
        Service.objects.create(
            user=request.user,
            name=name,
            description=description,
            price=price,
            duration=duration,
            image_url=file_url
        )
    
    return render(request, 'service/create_service.html')

@login_required
def service_update(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        images = request.FILES.get('images')

        if images:
            unique_file_name = random.randint(100_000_000, 999_999_999)
            ext = os.path.splitext(images.name)[1] or ".jpg"
            filename = f'name-{int(time.time())}-{unique_file_name}{ext}' 
            upload_path = os.path.join(settings.BASE_DIR,'static','images',filename)

            with open(upload_path, 'wb+') as dest:
                for chunk in images.chunks():
                    dest.write(chunk)

            file_url = f'static/images/{filename}'

        else:
            file_url = None

        users = request.user

@login_required
def service_delete(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        images = request.FILES.get('images')

        if images:
            unique_file_name = random.randint(100_000_000, 999_999_999)
            ext = os.path.splitext(images.name)[1] or ".jpg"
            filename = f'name-{int(time.time())}-{unique_file_name}{ext}' 
            upload_path = os.path.join(settings.BASE_DIR,'static','images',filename)

            with open(upload_path, 'wb+') as dest:
                for chunk in images.chunks():
                    dest.write(chunk)

            file_url = f'static/images/{filename}'

        else:
            file_url = None

        users = request.user
