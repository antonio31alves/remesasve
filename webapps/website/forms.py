from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from webapps.dashboard.models import  UserProfile

# class LoginForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = [
# 			'username',
# 			'password',
# 		]
		
# 		labels = {
# 			'username' : 'Username',
# 			'password' : 'Password',

# 		}




class SignUpForm(UserCreationForm):
	class Meta:
		model=UserProfile
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			# 'dob',
			# 'phone',
			# 'country',
			# 'city',
			# 'postcode',
		]
		labels = {
			'username' : 'Username',
			'first_name' : 'Nombres',
			'last_name' : 'Apellidos',
			'email' : 'Email',
			# 'dob' : 'Fecha de nacimiento',
			# 'phone' : 'Telefono',
			# 'country':'Pais',
			# 'city':'Ciudad',
			# 'postcode' : 'Codigo postal',
		}