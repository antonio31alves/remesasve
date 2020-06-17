from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from webapps.dashboard.models import  UserProfile


class SignUpForm(UserCreationForm):
	class Meta:
		model=UserProfile
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			
		]
		labels = {
			'username' : 'Username',
			'first_name' : 'Nombres',
			'last_name' : 'Apellidos',
			'email' : 'Email',
		}

	