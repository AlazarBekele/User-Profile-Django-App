from django.shortcuts import render
from .models import Profile

# Create your views here.

def index (request):

    profile = Profile.objects.exclude(user=request.user)

    context= {
        'profile' : profile
    }

    return render (request, 'Profile_list.html', context=context)