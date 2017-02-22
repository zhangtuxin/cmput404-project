from django.http import HttpResponse
from django.shortcuts import render
import os

def home(request):
    return render(request, 'profile/upload.html', {'what':'Django File Upload'})

def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")

    return HttpResponse("Failed")

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
