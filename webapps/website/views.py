from django.contrib.auth import login as dj_login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from webapps.website.forms import SignUpForm
from django.contrib.auth.forms import PasswordResetForm
from django.http import HttpRequest



# from django.http import HttpResponse


# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .token_generator import account_activation_token
# from django.core.mail import EmailMessage






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
					password = form.cleaned_data.get('password1')
					user = authenticate(username=username, password=password)
					dj_login(request, user)
					return redirect('dashboard')
			# if form.is_valid():
			# 	user = form.save(commit=False)
			# 	user.is_active = False
			# 	user.save()
			# 	current_site = get_current_site(request)
			# 	email_subject = 'Activate Your Account'
			# 	message = render_to_string('email_activate_account.html', {
			# 	    'user': user,
			# 	    'domain': current_site.domain,
			# 	    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
			# 	    'token': account_activation_token.make_token(user),
			# 	})
			# 	to_email = form.cleaned_data.get('email')
			# 	email = EmailMessage(email_subject, message, to=[to_email])
			# 	email.send()
			# 	return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
			# else:
			# 	form = UserSignUpForm()
			# return render(request, 'signup.html', {'form': form})




	#SI SE OPRIME EL BOTON DE INICIAR SESION 
		if request.POST.get('log-in-action') == 'True':
				#OBTENGO EL USURIO Y PASSWORD PARA AUTENTICARLOS Y REDIRECCIONAR AL SISTEMA.
				username = request.POST.get('usernamelogin')
				password = request.POST.get('passwordlogin')

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
		if request.POST.get('password-reset-action') == 'True':
			form = PasswordResetForm({'email': request.POST.get('username-reset')})
			if form.is_valid():
				request = HttpRequest()
				request.META['SERVER_NAME'] = 'remesasve.herokuapp.com'
				request.META['SERVER_PORT'] = '80'
				
				form.save(
				request= request,
				use_https=True,
				from_email="support.remesasve.com", 
				email_template_name='email/password_reset_email.html')
				send_message = True
				contexto = {'send_message':send_message}
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

def login(request):
	return render(request, 'website/login.html')

def signup(request):
	return render(request, 'website/signup.html')


