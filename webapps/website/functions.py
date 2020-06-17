from django.shortcuts import render, redirect
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth import login as dj_login, authenticate

from webapps.dashboard.models import UserProfile



def send_mail(request, mail, template_name):
	if template_name == 'password-reset':
		route = get_template('email/password_reset_email.html')
		subject = 'Recuperación de contraseña'
	if template_name == 'active-account':
		route = get_template('email/activate_email.html')
		subject = 'Activación de cuenta'
	template = route
	user = User.objects.get(username=mail)
	username = user.username
	user_id= urlsafe_base64_encode(force_bytes(user.pk))
	token = default_token_generator.make_token(user)
	current_site = get_current_site(request)
	domain = current_site.domain
	contexto = {
	'username':username,
	'uid': user_id,
	'token':token,
	'domain':domain
	}
	content = template.render(contexto)
	email = EmailMultiAlternatives(
		subject,
		'remesasve',
		settings.EMAIL_HOST_USER,
		[mail]
	)
	email.attach_alternative(content, 'text/html')
	email.send()
	


def activate_account(request, uidb64, token):
	pk= urlsafe_base64_decode(uidb64)
	user = User.objects.get(pk=int(pk))
	user_is_active =  UserProfile.objects.get(pk=int(pk))
	if user_is_active.email_active == True:
		account_active = 'True'
		contexto = {
		'account_active':account_active,
		'username':user.username,
		}
		return render(request, 'website/inicio.html', contexto)
	else:
		active = UserProfile.objects.filter(pk=int(pk)).update(email_active=True)
		if str(user.username) == str(request.user):
			return redirect('dashboard')
		else:
			modal_account_active = 'True'
			contexto = {
			'modal_account_active':modal_account_active,
			'username':user.username,
			}
			return render(request, 'website/inicio.html', contexto)





