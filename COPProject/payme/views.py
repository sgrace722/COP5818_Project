from django.shortcuts import render
from .models import LOGIN
from .forms import LoginForm
# Create your views here.


form = LoginForm()


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name_input = form.cleaned_data[user_name_input]
            user_password_input = form.cleaned_data[user_password_input]
    return render(request, "login_screen.html", {"method": request.method, "form": form})

# referenced for additional help
# https://openclassrooms.com/en/courses/7107341-intermediate-django/7263317-create-a-login-page-with-a-function-based-view
