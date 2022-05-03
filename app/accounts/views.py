from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import DonorCreationForm, DonorAuthenticationForm

User = get_user_model()


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = DonorCreationForm
    success_url = reverse_lazy('login')


class DonorLoginView(LoginView):
    form_class = DonorAuthenticationForm
    template_name = 'registration/login.html'

    def form_invalid(self, form):
        """If the form is invalid, check if user is in database if True render the invalid form,
            else redirect to register."""
        username = form.cleaned_data.get('username')
        check_user_in_database = get_user_model().objects.filter(email=username).exists()
        if check_user_in_database is False:
            return redirect('register')
        else:
            return self.render_to_response(self.get_context_data(form=form))
