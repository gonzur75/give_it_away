from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django import forms
from django.forms import ModelForm
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


class AddDonationForm(ModelForm):
    class Meta:
        model = Donation
        exclude = ['user', 'institution']
        widgets = {
            'pick_up_date': forms.DateInput(attrs={'type': 'date'}),
            'pick_up_time': forms.TimeInput(attrs={'type': 'time'}),
            'pick_up_comment': forms.Textarea(attrs={'rows': 5}),
            'phone_number': forms.TextInput(attrs={'type': 'phone'}),
        }

class AddDonationView(LoginRequiredMixin, CreateView):
    template_name = 'home/add-donation_form.html'
    model = Donation
    form_class = AddDonationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        context.update({
            'categories': categories,
            'institutions': institutions,
        })
        return context
