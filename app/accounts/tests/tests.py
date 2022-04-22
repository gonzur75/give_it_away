# Create your tests here.
import pytest
from django.db import IntegrityError
from django.urls import reverse_lazy


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
        django_user_model.objects.create_super_user(
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
    assert response.status_code == 200
