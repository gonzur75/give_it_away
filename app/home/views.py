from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from home.models import Donation


class LandingPageView(TemplateView):
    template_name = 'home/landing-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        number_of_bags = sum([bag for bag in Donation.objects.values('quantity')])
        number_of_institution = sum(set([institution for institution in Donation.objects.values('institution')]))
        context.update({
            'number_of_organisation': number_of_institution,
            'number_of_bags': number_of_bags
        })
        return context


class AddDonationView(TemplateView):
    template_name = 'home/add-donation-form.html'
