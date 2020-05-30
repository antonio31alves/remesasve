from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy




class Dashboard(TemplateView):
	template_name = "dashboard/index.html"
	success_url = reverse_lazy('dashboard')


class Profile(TemplateView):
	template_name = "dashboard/profile/index.html"
	success_url = reverse_lazy('profile')