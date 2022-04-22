import pytest
from django.test import Client


@pytest.fixture(scope='function')
def user(django_user_model):
    user = django_user_model.objects.create_user(
        email="test@test.com",
        password='TestPass123'
    )
    yield user


@pytest.fixture(scope='function')
def superuser(django_user_model):
    superuser = django_user_model.objects.create_super_user(
        email="test@test.com",
        password='TestPass123'
    )
    yield superuser


@pytest.fixture
def client():
    client = Client()
    return client
