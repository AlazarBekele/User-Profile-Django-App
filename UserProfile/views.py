from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
# Create your views here.

def index (request):

    if request.user.is_authenticated:
        
        profile = Profile.objects.exclude(user=request.user)
        context= {
            'profile' : profile
        }
        return render (request, 'Profile_list.html', context=context)
    
    else:

        messages.success(request, "Must Have logged in to access this page...")

        return redirect ('navbarPage')
    
def home (request):

    return render (request, 'index.html')


def navbar (request):

    return render (request, 'newhome.html')

def profile (request, pk):

    if request.user.is_authenticated:

        profile = Profile.objects.get(user_id=pk)
        context = {
            'profile' : profile
        }
        return render (request, 'profile_html.html', context=context)
    
    else:

        messages.success(request, "Must Have logged in to access this page...")

        return redirect ('navbarPage')