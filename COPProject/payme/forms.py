from django import forms
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['paypalemail', 'bio', 'profile_picture']  # Include additional fields as needed

CURRENCY_CHOICES = (
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('IDR', 'IDR'),
    ('JPY', 'JPY'),
)

class GenerateForm(forms.Form):
    amount = forms.DecimalField(label='Amount', min_value=0.01)
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, initial='USD', required=True)
