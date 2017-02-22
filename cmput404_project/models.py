from django.db import models

class Profile(models.Model):
    name = models.FileField(null=True, blank=True)
    # "upload_to" indicates where the picture will be saved on hard drive
    picture = models.ImageFiled(upload_to = 'pictures')

    class Meta:
        db_table = "profile"
