from django.urls import path

from .views import LandingPageView

app_name = 'home'

urlpatterns = [
    path('landing', LandingPageView.as_view(), name='landing_page'),
]