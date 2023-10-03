from django import forms


class LoginForm(forms.Form):
    user_name_input = forms.CharField()
    user_password_input = forms.CharField(widget=forms.PasswordInput)
# referenced page 302 in textbook CH6 on forms
