from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Institution(models.Model):
    class Meta:
        ordering = ['-name']
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


# def get_sentinel_institution():
#     return Institution.objects.get_or_create(name='deleted')[0]


class Donation(models.Model):
    quantity = models.SmallIntegerField()
    categories = models.ManyToManyField('Category')
    institution = models.ForeignKey(
        'Institution',
        on_delete=models.SET_NULL,
        null=True,
    )
    address = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=255)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
