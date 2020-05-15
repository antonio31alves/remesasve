from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import Dashboard


urlpatterns = [
	path('', login_required(Dashboard.as_view(), redirect_field_name='/'), name="dashboard"),

]