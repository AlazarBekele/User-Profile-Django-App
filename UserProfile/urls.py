from django.urls import path
from .views import index, home, navbar, profile

urlpatterns = [
    path ('home/', index, name='profile_list'),
    path ('', home, name='home'),
    path ('nav/', navbar, name='navbarPage'),
    path ('profile/<int:pk>', profile, name='profile_id')
]
