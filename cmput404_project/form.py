# https://www.tutorialspoint.com/django/django_file_uploading.htm

from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(max_length = 100)
    picture = forms.ImageFileds() # ImageFiled make sure the upload is an image
    
