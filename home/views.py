from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
import random , os , time

@login_required
def home(request):
    return render(request, 'home/index.html')

#@login_required
#def create_service(request):
    #if request.method == 'POST':
       # name = request.POST.get('name')
        #description = request.POST.get('description')
        #price = request.POST.get('price')
        #duration = request.POST.get('duration')
        #images = request.FILES.get('images')

        #if images:
         #   unique_file_name = random.randint(100_000_000, 999_999_999)
          #  ext = os.path.splitext(images.name)[1] or ".jpg"
           # filename = f'name-{int(time.time())}-{unique_file_name}{ext}' 
            #upload_path = os.path.join(settings.BASE_DIR,'static','images',filename)

            #with open(upload_path, 'wb+') as dest:
             #   for chunk in images.chunks():
              #      dest.write(chunk)

            #file_url = f'static/images/{filename}'

        #else:
         #   file_url = None

        #users = request.user

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
