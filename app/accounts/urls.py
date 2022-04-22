from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = ''


class RegisterView(TemplateView):
    template_name = 'accounts/register.html'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegisterView.as_view(), name='register'),


]