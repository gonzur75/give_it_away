import pytest
from django.db.models import Count, Sum
from django.urls import reverse_lazy

from home.models import Donation, Institution



@pytest.mark.django_db
def test_landing_page_view(landing_page_get_response):
    assert landing_page_get_response.status_code == 200


def test_add_donation_view(client):
    response = client.get(reverse_lazy('home:add_donation'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_display_number_of_donated_bags(set_up, landing_page_get_response):
    number_of_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
    look_up_text = f'<em id="number_of_bags">{number_of_bags}</em>'
    assert look_up_text in landing_page_get_response.content.decode('UTF-8')


@pytest.mark.django_db
def test_display_number_of_supported_institution(set_up, landing_page_get_response):
    # len(set([institution for institution in Donation.objects.values_list('institution')]))
    number_of_organisations = Donation.objects.filter('')       # użyj count
    look_up_text = f'<em id="number_of_organisation">{number_of_organisations}</em>'
    assert look_up_text in landing_page_get_response.content.decode('UTF-8')


@pytest.mark.django_db
def test_context_list_of_fundations_for_landing_page(set_up, landing_page_get_response):
    list_of_foundations = list(Institution.objects.filter(type='FU'))
    assert list_of_foundations in landing_page_get_response.context['list_of_foundations']


