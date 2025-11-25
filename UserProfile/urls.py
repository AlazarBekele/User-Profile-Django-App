from django.urls import path
from .views import index, home, navbar

urlpatterns = [
    path ('home/', index, name='profile_list'),
    path ('', home, name='home'),
    path ('nav/', navbar, name='navbarPage')
]
