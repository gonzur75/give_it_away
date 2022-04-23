import pytest
from home.models import Category, Institution

from app.home.tests.utils import fake_institution_data, get_choice, get_categories, faker


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
    fake_data_without_type = fake_institution_data().pop('type')
    test_institution = Institution.objects.create(**fake_data_without_type)
    # Direct assignment to the forward side of a many-to-many set is
    # prohibited. Use categories.set() instead.
    test_institution.categories.set(get_categories())
    assert Institution.objects.last().type == 'FU'
