from django.urls import path, include

from .views import RegisterView, DonorLoginView, DonorDetailView

app_name = ''

urlpatterns = [
    path('accounts/login/', DonorLoginView.as_view(), name='login'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/user_detail/<int:pk>', DonorDetailView.as_view(), name='user_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]