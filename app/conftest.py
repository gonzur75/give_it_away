import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse_lazy

from home.models import Institution, Donation, Category
from home.tests.utils import fake_institution_data, fake, get_categories, fake_donation_data

TEST_USERNAME = "TestUser"
TEST_EMAIL = "test@test.com"
TEST_PASSWORD = 'TestPass123'


@pytest.fixture(scope='function')
def user(django_user_model):
    user = django_user_model.objects.create_user(
        email="test@test.com",
        password='TestPass123'
    )
    yield user


@pytest.fixture(scope='function')
def custom_user():
    custom_user, created = get_user_model().objects.get_or_create(
        email="test@test.com",
    )
    if created:
        custom_user.set_password(TEST_PASSWORD)
        custom_user.save()

    return custom_user


@pytest.fixture(scope='function')
def superuser(django_user_model):
    superuser = django_user_model.objects.create_superuser(
        email="test@test.com",
        password='TestPass123'
    )
    yield superuser


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture(scope='function')
def landing_page_get_response(client):
    return client.get(reverse_lazy('home:landing_page'))


@pytest.fixture(scope='function')
def user_logged_in(user, client):
    client.login(email=TEST_EMAIL, password=TEST_PASSWORD)


@pytest.fixture
def set_up(custom_user):
    for _ in range(5):
        Category.objects.create(name=fake.name())

    for x in range(3):
        choices = ['FU', 'OP', 'ZL']
        data = fake_institution_data()
        data['type'] = choices[x]
        institution = Institution.objects.create(**data)
        institution.categories.add(Category.objects.create(name='test'))

    for _ in range(10):
        donation_object = Donation.objects.create(**fake_donation_data(custom_user))
        donation_object.categories.set(get_categories())
