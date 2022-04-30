from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import PasswordInput, EmailInput
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class DonorCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': _('Imię')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('Nazwisko')}),
            'email': forms.EmailInput(attrs={'placeholder': _('Email')}),
        }

    # The Meta.widgets option doesn't apply to fields that were declared in the form.
    # See the note in the docs. In this case, password1 and password2 are declare on the UserCreationForm
    # (they aren't model fields), therefore you can't use them in widgets.
    #
    def __init__(self, *args, **kwargs):
        super(DonorCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': _('Hasło')})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': _('Powtórz hasło')})


class DonorAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(DonorAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = EmailInput(attrs={'placeholder': _('Email')})
        self.fields['password'].widget = PasswordInput(attrs={
            'placeholder': _('Hasło'),
            'autocomplete': 'current-password'
        })

