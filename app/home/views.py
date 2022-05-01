from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView
from home.models import Donation, Institution, Category


class LandingPageView(TemplateView):
    template_name = 'home/landing-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


class AddDonationView(LoginRequiredMixin, CreateView):
    template_name = 'home/add-donation_form.html'
    model = Donation
    fields = [
        'quantity', 'categories', 'institution', 'address', 'phone_number',
        'city', 'zip_code', 'pick_up_date', 'pick_up_time', 'pick_up_comment'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context.update({
            'categories': categories,

        })
        return context
