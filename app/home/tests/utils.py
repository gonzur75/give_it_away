import random

from django.utils.translation import gettext_lazy as _
from faker import Faker


def fake_institution_data():
    fake_data = {
        'name': 'Test name',
        'description': faker.paragraph(nb_sentences=2),
        'type': get_choice(),
    }
    return fake_data


def get_choice():
    INSTITUTION_TYPE_CHOICES = [
        ('FU', _('fundacja')),
        ('OP', _('organizacja pozarządowa')),
        ('ZL', _('zbiórka lokalna')),
    ]
    choice, txt = random.choice(INSTITUTION_TYPE_CHOICES)
    return choice


def get_categories():
    for _ in range(3):
        Category.objects.create(name=faker.name())
    return Category.objects.all()


faker = Faker("pl_PL")
