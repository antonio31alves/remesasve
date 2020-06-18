from django.contrib.auth import login as dj_login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from webapps.website.forms import SignUpForm
from webapps.website.functions import send_mail


# from django.contrib.auth.forms import PasswordResetForm


# from django.urls import reverse_lazy

# from django.http import HttpRequest
# from django.http import HttpResponse




# from django.conf import settings
# from django.template.loader import get_template
# from django.core.mail import EmailMultiAlternatives
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.sites.requests import RequestSite
# from django.contrib.sites.shortcuts import get_current_site







class inicio(CreateView):
	form_class = SignUpForm
	template_name = "website/inicio.html"

	# REGISTRO DEL USUARIO
	def post(self, request, *args, **kwars):
		form = SignUpForm(request.POST)
		if request.POST.get('sign-up-create') == 'True':
			user_exists = User.objects.filter(username=request.POST.get('username')).exists()
			if user_exists == True:
				user_exists_error = True
				contexto = {'user_exists_error':user_exists_error}
				return render(request, 'website/inicio.html', contexto)
			else:
				if form.is_valid():
					save = form.save(commit=False)
					save.email = request.POST.get('username')
					save = form.save()
					#OBTENGO EL USURIO Y PASSWORD PARA AUTENTICARLOS Y REDIRECCIONAR AL SISTEMA LUEGO DE CREAR EL USUARIO.
					username = form.cleaned_data.get('username')
					password = form.cleaned_data.get('password2')
					print(password)
					user = authenticate(username=username, password=password)
					send_mail(request, request.POST.get('username'), 'active-account')
					dj_login(request, user)
					return redirect('dashboard')
				else:
					contexto = {
					'form':form,
					# 'password1' :request.POST.get('password1'),
					# 'password2' :request.POST.get('password2')
					}
					return render(request, 'website/inicio.html', contexto)

		#SI SE OPRIME EL BOTON DE INICIAR SESION 
		if request.POST.get('log-in-action') == 'True' or request.POST.get('log-in-action-active-account') == 'True':
			#OBTENGO EL USURIO Y PASSWORD PARA AUTENTICARLOS Y REDIRECCIONAR AL SISTEMA.
			username = request.POST.get('usernamelogin')
			if request.POST.get('log-in-action') == 'True':
				password = request.POST.get('passwordlogin')
			if request.POST.get('log-in-action-active-account') == 'True':
				# username = request.POST.get('usernamelogin')
				password = request.POST.get('passwordloginactivate')

			verify_user = User.objects.filter(username=username).exists()
			if verify_user == False:
				error_user = True
				contexto = {'error_user':error_user}
				return render(request, 'website/inicio.html', contexto)
			else:
				user = authenticate(username=username, password=password)
				if user is not None:
					dj_login(request, user)
					return redirect('dashboard')
				else:
					error_password = True
					contexto = {'error_password':error_password}
					return render(request, 'website/inicio.html', contexto)

		# #SI SE OPRIME EL BOTON DE INICIAR SESION ACTIVE ACCOUNT
		# if request.POST.get('log-in-action-active-account') == 'True':
		# 	print('holaa')
		# 	#OBTENGO EL USURIO Y PASSWORD PARA AUTENTICARLOS Y REDIRECCIONAR AL SISTEMA.
		# 	username = request.POST.get('usernamelogin')
		# 	password = request.POST.get('passwordloginactivate')

		# 	verify_user = User.objects.filter(username=username).exists()
		# 	if verify_user == False:
		# 		error_user = True
		# 		contexto = {'error_user':error_user}
		# 		return render(request, 'website/inicio.html', contexto)
		# 	else:
		# 		user = authenticate(username=username, password=password)
		# 		if user is not None:
		# 			dj_login(request, user)
		# 			return redirect('dashboard')
		# 		else:
		# 			error_password = True
		# 			contexto = {'error_password':error_password}
		# 			return render(request, 'website/inicio.html', contexto)

		if request.POST.get('password-reset-action'):
			user = User.objects.filter(username=request.POST.get('username-reset')).exists()
			if user:
				send_mail(request, request.POST.get('username-reset'), 'password-reset')
				send_message = True
				contexto = {'send_message':send_message}
				return render(request, 'website/inicio.html', contexto)
				
			else:
				error_user = True
				contexto = {'error_user':error_user}
				return render(request, 'website/inicio.html', contexto)
		return redirect('inicio')



def quienes_somos(request):
	value_menu_active = '1'
	contexto = {'value_menu_active':value_menu_active}
	return render(request, 'website/quienes_somos.html', contexto)

def preguntas_frecuentes(request):
	value_menu_active = '2'
	contexto = {'value_menu_active':value_menu_active}
	return render(request, 'website/preguntas_frecuentes.html', contexto)

def tipo_cambio(request):
	value_menu_active = '3'
	contexto = {'value_menu_active':value_menu_active}
	return render(request, 'website/tipo_cambio.html', contexto)

def contactenos(request):
	return render(request, 'website/contactenos.html')

def login_app(request):
	return render(request, 'website/login.html')

def home_app(request):
	return render(request, 'website/home_app.html')

def login_app(request):
	return render(request, 'website/login.html')

def signup(request):
	return render(request, 'website/signup.html')


