from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'username',
			'password',
		]
		
		labels = {
			'username' : 'Username',
			'password' : 'Password',

		}




class SignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			)
		labels = {
			'username':'Username',
			'first_name':'Nombres',
			'last_name': 'Apellidos',
			'email':'Email',
		}