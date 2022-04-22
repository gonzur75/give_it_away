from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'home/landing-page.html'


class AddDonationView(TemplateView):
    template_name = 'home/add-donation-form.html'
