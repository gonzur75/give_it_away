import pytest
from home.models import Category, Institution, Donation


from app.home.tests.utils import fake_institution_data, get_categories, fake_donation_data


@pytest.mark.django_db
def test_category_model_object_create():
    test_category = Category.objects.create(
        name='Test name'
    )
    assert Category.objects.last() == test_category


@pytest.mark.django_db
def test_institution_model_object_create():
    test_institution = Institution.objects.create(**fake_institution_data())
    test_institution.categories.set(get_categories())
    assert Institution.objects.last() == test_institution


@pytest.mark.django_db
def test_institution_model_type_default():
    fake_data_without_type = fake_institution_data()
    fake_data_without_type.pop('type')
    test_institution = Institution.objects.create(**fake_data_without_type)
    # Direct assignment to the forward side of a many-to-many set is
    # prohibited. Use categories.set() instead.
    test_institution.categories.set(get_categories())
    assert Institution.objects.last().type == 'FU'


@pytest.mark.django_db
def test_donation_model_object_creation(user):
    test_donation_object = Donation.objects.create(**fake_donation_data(user))
    # Direct assignment to the forward side of a many-to-many set is
    # prohibited. Use categories.set() instead.
    test_donation_object.categories.set(get_categories())
    assert Donation.objects.last() == test_donation_object