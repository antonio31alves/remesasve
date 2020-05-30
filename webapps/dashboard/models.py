from django.db import models

from django.contrib.auth.models import User


#USER PROFILE
class UserProfile(User):
	name=models.CharField(max_length=150, blank=True, null=True)
	surname=models.CharField(max_length=150, blank=True, null=True)
	dob=models.DateField(blank=True, null=True)	
	phone=models.CharField(max_length=150, blank=True, null=True)
	country=models.CharField(max_length=150, blank=True, null=True)
	city=models.CharField(max_length=150, blank=True, null=True)
	address=models.CharField(max_length=150, blank=True, null=True)
	postcode=models.CharField(max_length=150, blank=True, null=True)
	email_active=models.BooleanField(default=0)
	complete_perfil=models.BooleanField(default=0)


