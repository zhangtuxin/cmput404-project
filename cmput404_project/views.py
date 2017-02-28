import os
from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile

def profile(request,userName):
    myUser = Profile.objects.all()
    context ={'userName':userName, 'myUser':myUser}
    return render(request, 'profile/profile.html',context)
    #return render(request, 'profile/profile.html')
