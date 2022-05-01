import pprint

import pytest
from django.db.models import Count, Sum
from django.urls import reverse_lazy

from home.models import Donation, Institution, Category


@pytest.mark.django_db
def test_landing_page_view(landing_page_get_response):
    assert landing_page_get_response.status_code == 200


@pytest.mark.django_db
def test_display_number_of_donated_bags(set_up, landing_page_get_response):
    number_of_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
    look_up_text = f'<em id="number_of_bags">{number_of_bags}</em>'
    assert look_up_text in landing_page_get_response.content.decode('UTF-8')


@pytest.mark.django_db
def test_display_number_of_supported_institution(set_up, landing_page_get_response):
    # len(set([institution for institution in Donation.objects.values_list('institution')]))
    number_of_organisations = Donation.objects.distinct('institution').count()  # użyj count
    look_up_text = f'<em id="number_of_organisation">{number_of_organisations}</em>'
    assert look_up_text in landing_page_get_response.content.decode('UTF-8')


@pytest.mark.django_db
def test_context_list_of_foundations_for_landing_page(set_up, landing_page_get_response):
    foundation = Institution.objects.filter(type='FU').first()
    assert foundation in landing_page_get_response.context['list_of_foundations']


@pytest.mark.django_db
def test_context_list_of_organizations_for_landing_page(set_up, landing_page_get_response):
    organisation = Institution.objects.filter(type='OP').first()
    assert organisation in landing_page_get_response.context['list_of_organizations']


@pytest.mark.django_db
def test_context_list_of_collections_for_landing_page(set_up, landing_page_get_response):
    collection = Institution.objects.filter(type='ZL').first()
    assert collection in landing_page_get_response.context['list_of_collections']


def test_add_donation_view(client):
    response = client.get(reverse_lazy('home:add_donation'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_donation_view_displaying_categories(user_logged_in, set_up, client):
    category_name = Category.objects.first().name
    response = client.get(reverse_lazy('home:add_donation'), follow=True)
    pp = pprint.PrettyPrinter(width=155, compact=True)
    pp.pprint(response.content.decode('utf-8'))

    assert category_name in response.content.decode('Utf-8')
