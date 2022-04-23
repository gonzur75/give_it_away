from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Institution(models.Model):
    FOUNDATION = 'FU'
    ORGANISATION = 'OP'
    COLLECTION = 'ZL'
    INSTITUTION_TYPE_CHOICES = [
        ('FU', _('fundacja')),
        ('OP', _('organizacja pozarządowa')),
        ('ZL', _('zbiórka lokalna')),
    ]

    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=255)
    type = models.CharField(
        max_length=2,
        choices=INSTITUTION_TYPE_CHOICES,
        default=FOUNDATION,
    )
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.name

