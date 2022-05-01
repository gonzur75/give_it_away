# Create your tests here.
import pprint

import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.urls import reverse_lazy

from conftest import TEST_EMAIL, TEST_PASSWORD


# pp = pprint.PrettyPrinter(width=155, compact=True)
#     pp.pprint(response.content.decode('utf-8'))

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


@pytest.mark.django_db
def test_landing_page_view_has_user_menu(user, client):
    client.login(username=TEST_EMAIL, password=TEST_PASSWORD)
    response = client.get('/')
    check_text = f'Witaj {TEST_EMAIL}'
    assert check_text in response.content.decode('utf-8')


@pytest.mark.django_db
def test_user_loging_in(user, client):
    response = client.post('/accounts/login/', {
        'email': TEST_EMAIL,
        'password': TEST_PASSWORD,
    })
    assert get_user_model().objects.last().is_authenticated


@pytest.mark.django_db
def test_none_existing_user_redirect_to_registration(client):
    response = client.post('/accounts/login/', {
        'email': TEST_EMAIL,
        'password': TEST_PASSWORD,
    }, follow=True)
    assert '/accounts/register/' in response.content.decode('utf-8')


def test_register_view(client):
    response = client.get('/accounts/register/')
    assert response.status_code == 200


@pytest.mark.django_db
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
