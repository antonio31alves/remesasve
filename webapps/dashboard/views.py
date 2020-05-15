from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy




class Dashboard(TemplateView):
	template_name = "dashboard/index.html"
	success_url = reverse_lazy('dashboard')