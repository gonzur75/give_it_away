from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django import forms
from django.forms import ModelForm
from django.http import JsonResponse
from django.shortcuts import render, redirect

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




class AddDonationView(LoginRequiredMixin, TemplateView):
    template_name = 'home/add-donation_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        context.update({
            'categories': categories,
            'institutions': institutions,
        })
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        institution = Institution.objects.get(name=data['organization'])
        donation = Donation.objects.create(
            quantity=data['bags'],
            institution=institution,
            address=data['address'],
            phone_number=data['phone'],
            city=data['city'],
            zip_code=data['postcode'],
            pick_up_date=data['data'],
            pick_up_time=data['time'],
            pick_up_comment=data['more_info'],
            user=request.user
        )
        donation.categories.set(data['categories'])
        response = redirect('home:form_confirmation')
        return response


class FormConfirmationView(LoginRequiredMixin, TemplateView):
    template_name = 'home/form-confirmation.html'
