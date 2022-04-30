from django.urls import path, include

from .views import RegisterView, DonorLoginView

app_name = ''

urlpatterns = [
    path('accounts/login/', DonorLoginView.as_view(), name='login'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]