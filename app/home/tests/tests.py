# Create your tests here.
import pytest
from django.urls import reverse_lazy

from home.models import Category


def test_landing_page_view(client):
    response = client.get(reverse_lazy('home:landing_page'))
    assert response.status_code == 200


def test_add_donation_view(client):
    response = client.get(reverse_lazy('home:add_donation'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_model_object_create():
    test_category = Category.objects.create(
        name='Test name'
    )

    assert Category.objects.last() == test_category
