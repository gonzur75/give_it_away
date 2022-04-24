import random

from django.utils.translation import gettext_lazy as _
from faker import Faker

from home.models import Category, Institution




def fake_institution_data():
    fake_data = {
        'name': fake.name(),
        'description': fake.paragraph(nb_sentences=2),
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
    categories = Category.objects.all()
    return random.choice(categories)


fake = Faker("pl_PL")


def fake_donation_data(user):
    fake_data = {
        'quantity': random.randint(1, 10),
        'institution': get_institution(),
        'address': fake.street_address(),
        'phone_number': fake.phone_number(),
        'city': fake.city(),
        'zip_code': fake.postcode(),
        'pick_up_date': fake.date(),
        'pick_up_time': fake.time(),
        'pick_up_comment': fake.paragraphs(nb=2),
        'user': user
    }
    return fake_data


def get_institution():
    return Institution.objects.create(**fake_institution_data())
