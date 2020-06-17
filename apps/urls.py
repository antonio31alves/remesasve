# from django.contrib import admin
# from django.contrib.auth.views import logout_then_login
# from django.urls import path, include
# from django.views.generic import RedirectView
# from django.contrib.auth import views as auth_views
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns = [
#     #NATIVE FROM DJANGO
#     path('admin/', admin.site.urls),
#     path('logout', logout_then_login, name='logout'),
#     path('accounts/login/', RedirectView.as_view(url='/')),
#       path('password_reset_form/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='email/password_reset_form.html'), name="password_reset_form"),
#     # 1- URLS WEBSITE
#     path(r'', include('webapps.website.urls'), name="website"),
#     # 2- URLS ADMIN DASHBOARD SYSTEM
#     path(r'dashboard/', include('webapps.dashboard.urls'), name="dashboard"),
# ]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.contrib.auth.views import logout_then_login
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #NATIVE FROM DJANGO
    path('admin/', admin.site.urls),
    path('logout', logout_then_login, name='logout'),
    path('accounts/login/', RedirectView.as_view(url='/')),
    path('password_reset_form/<uidb64>/<token>', 
        auth_views.PasswordResetConfirmView.as_view(template_name='email/password_reset_form.html'), 
        name="password_reset_form"),
    path('password_reset_complete/', 
        RedirectView.as_view(url='/'), 
        name="password_reset_complete"), 
    # 1- URLS WEBSITE
    path(r'', include('webapps.website.urls'), name="website"),
    # 2- PWA
    path(r'', include('pwa.urls')),
    # 3- URLS ADMIN DASHBOARD SYSTEM
    path(r'dashboard/', include('webapps.dashboard.urls'), name="dashboard"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
