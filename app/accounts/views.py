from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import DonorCreationForm

User = get_user_model()


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = DonorCreationForm
    success_url = reverse_lazy('login')
