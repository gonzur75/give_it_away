from django.urls import path, include

from .views import RegisterView

app_name = ''

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegisterView.as_view(), name='register'),


]