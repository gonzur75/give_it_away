from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class DonorCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'first_name':  forms.TextInput(attrs={'placeholder': _('Imię')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('Nazwisko')}),
            'email': forms.EmailInput(attrs={'placeholder': _('Email')}),
            'password1': forms.PasswordInput(attrs={'placeholder': _('Hasło')}),
            'password2': forms.PasswordInput(attrs={'placeholder': _('Powtórz hasło')}),

        }
 # 'ingredients': forms.Textarea(attrs={'class': "w-100 p-1", 'rows': 10}),