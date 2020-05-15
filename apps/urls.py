"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import logout_then_login
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #NATIVE FROM DJANGO
    path('admin/', admin.site.urls),
    path('logout', logout_then_login, name='logout'),
    path('accounts/login/', RedirectView.as_view(url='/')),
    # 1- URLS WEBSITE
    path(r'', include('webapps.website.urls'), name="website"),
    # 2- URLS ADMIN DASHBOARD SYSTEM
    path(r'dashboard/', include('webapps.dashboard.urls'), name="dashboard"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
