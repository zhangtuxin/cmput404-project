'''
References:
https://www.tutorialspoint.com/django/django_file_uploading.htm
https://github.com/axelpale/minimal-django-file-upload-example
https://docs.djangoproject.com/en/1.10/topics/http/file-uploads/
http://www.codepool.biz/django-upload-file.html
'''

from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(max_length = 100)
    picture = forms.ImageFileds() # ImageFiled make sure the upload is an image
