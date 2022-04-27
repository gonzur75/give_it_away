# Create your tests here.
from pprint import pprint

import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.urls import reverse_lazy

from conftest import TEST_EMAIL, TEST_PASSWORD


def test_create_user(django_user_model, user):
    check_user = django_user_model.objects.last()
    assert check_user.email == "test@test.com"


def test_user_email_is_unique(django_user_model, user):
    with pytest.raises(IntegrityError):
        extra_user = django_user_model.objects.create_user(
            email="test@test.com",
            password='TestPass123'
        )


def test_user_is_not_staff(user):
    assert user.is_staff is False


def test_user_is_not_superuser(user):
    assert user.is_superuser is False


def test_user_is_active(user):
    assert user.is_active is True


def test_create_superuser(superuser):
    assert superuser.email == "test@test.com"


def test_superuser_email_is_unique(django_user_model, superuser):
    with pytest.raises(IntegrityError):
        django_user_model.objects.create_superuser(
            email="test@test.com",
            password='TestPass123'
        )


def test_superuser_is_staff(superuser):
    assert superuser.is_staff is True


def test_superuser_is_superuser(superuser):
    assert superuser.is_superuser is True


def test_superuser_is_active(superuser):
    assert superuser.is_active is True


def test_login_view(client):
    response = client.get('/accounts/login/')
    assert response.status_code == 200


def test_register_view(client):
    response = client.get('/accounts/register/')
    print(response.context)
    assert response.status_code == 302


def register_user_response(client):
    response = client.post('/accounts/register/', {
        'email': TEST_EMAIL,
        'password1': TEST_PASSWORD,
        'password2': TEST_PASSWORD,
    })
    return response


@pytest.mark.django_db
def test_register_user(client):
    response = register_user_response(client)
    assert response.status_code == 302
    user = get_user_model()
    assert user.objects.count() == 1

@pytest.mark.django_db
def test_register_user(client):
    response = register_user_response(client)
    assert '/accounts/login/' == response.url
