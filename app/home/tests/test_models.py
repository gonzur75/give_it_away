import random
from faker import Faker
import pytest
from django.utils.translation import gettext_lazy as _
from home.models import Category, Institution

faker = Faker("pl_PL")


@pytest.mark.django_db
def test_category_model_object_create():
    test_category = Category.objects.create(
        name='Test name'
    )
    assert Category.objects.last() == test_category


def get_categories():
    for _ in range(3):
        Category.objects.create(name=faker.name())
    return Category.objects.all()


def get_choice():
    INSTITUTION_TYPE_CHOICES = [
        ('FU', _('fundacja')),
        ('OP', _('organizacja pozarządowa')),
        ('ZL', _('zbiórka lokalna')),
    ]
    choice, txt = random.choice(INSTITUTION_TYPE_CHOICES)
    return choice


@pytest.mark.django_db
def test_institution_model_object_create():
    test_institution = Institution.objects.create(
        name='Test name',
        description=faker.paragraph(nb_sentences=2),
        type=get_choice(),
    )
    test_institution.categories.set(get_categories())
    assert Institution.objects.last() == test_institution


@pytest.mark.django_db
def test_institution_model_type_default():
    test_institution = Institution.objects.create(
        name='Test name',
        description=faker.paragraph(nb_sentences=2),
    )
    # Direct assignment to the forward side of a many-to-many set is
    # prohibited. Use categories.set() instead.
    test_institution.categories.set(get_categories())
    assert Institution.objects.last().type == 'FU'
