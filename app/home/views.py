from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from home.models import Donation, Institution


class LandingPageView(TemplateView):
    template_name = 'home/landing-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # czy
        number_of_bags = Donation.objects.aggregate(quantity=Coalesce(Sum('quantity'), 0))['quantity']
        number_of_institution = Donation.objects.distinct('institution').count()
        list_of_foundations = Institution.objects.filter(type='FU')
        list_of_organizations = Institution.objects.filter(type='OP')
        list_of_collections = Institution.objects.filter(type='ZL')
        context.update({
            'number_of_organisation': number_of_institution,
            'number_of_bags': number_of_bags,
            'list_of_foundations': list_of_foundations,
            'list_of_organizations': list_of_organizations,
            'list_of_collections': list_of_collections
        })
        return context


class AddDonationView(TemplateView):
    template_name = 'home/add-donation-form.html'
