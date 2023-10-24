from django.shortcuts import render
from .models import LOGIN
from .forms import LoginForm, UrlForm
# Create your views here.


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name_input = form.cleaned_data['user_name_input']
            user_password_input = form.cleaned_data['user_password_input']
            try:
                user = LOGIN.objects.get(user_name=user_name_input, user_password=user_password_input)
                return render(request, 'logged_in.html', {'username': LOGIN.user_name})
            except LOGIN.DoesNotExist:
                form = LoginForm()
                form.add_error(None, 'Invalid Login credential')
    return render(request, "login_screen.html", { "form": form})


def url_page(request):
    form = UrlForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dollar_amount = form.cleaned_data['dollar_amount']
            return render(request, 'link_page.html')
    return render(request, "url_page.html", {"form": form} )



# referenced for additional help
# https://openclassrooms.com/en/courses/7107341-intermediate-django/7263317-create-a-login-page-with-a-function-based-view
