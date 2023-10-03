from django.shortcuts import render
from .models import LOGIN
from .forms import LoginForm
# Create your views here.


form = LoginForm()


def login_page(request):
    return render(request, "login_screen.html", {"method": request.method, "form": form})
