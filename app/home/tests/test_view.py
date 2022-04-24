import pytest
from django.urls import reverse_lazy

from home.models import Donation


def test_landing_page_view(landing_page_get_response):
    assert landing_page_get_response.status_code == 200


def test_add_donation_view(client):
    response = client.get(reverse_lazy('home:add_donation'))
    assert response.status_code == 200





@pytest.mark.django_db
def test_display_number_of_donated_bags(landing_page_get_response):
    number_of_bags = sum([bag for bag in Donation.objects.values('quantity')])
    look_up_text = f'<em id="number_of_bags">{number_of_bags}</em>'
    assert look_up_text in landing_page_get_response.content.decode('UTF-8')

@pytest.mark.django_db
def test_display_number_of_supported_institution(landing_page_get_response):
    number_of_organisations = sum(set([institution for institution in Donation.objects.values('institution')]))
    look_up_text = f'<em id="number_of_organisation">{number_of_organisations}</em>'
    assert look_up_text in landing_page_get_response.content.decode('UTF-8')
