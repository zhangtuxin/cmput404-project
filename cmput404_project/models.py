from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Profile(models.Model):
	userName = models.CharField(max_length=200)
	Email = models.CharField(max_length=200)
	Github = models.CharField(max_length=200)
	Bio = models.CharField(max_length=200)
	def __str__(self):
		return self.userName
