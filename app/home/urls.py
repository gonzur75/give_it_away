from django.urls import path

from .views import LandingPageView, AddDonationView, FormConfirmationView

app_name = 'home'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('add_donation/', AddDonationView.as_view(), name='add_donation'),
    path('form_confirmation/', FormConfirmationView.as_view(), name='form_confirmation'),
]