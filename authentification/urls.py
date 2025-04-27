from django.urls import path
from .views import login_view , register , logout_view , profile

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('profile/',profile, name='profile')
]