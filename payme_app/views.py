from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, UserProfileForm, PaymentRecordForm
from .models import UserProfile, PaymentRecord
from django.contrib.auth.decorators import login_required
import random
import string
from django.contrib.auth.forms import UserCreationForm

def generate_random_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))
def generate_unique_url():
    while True:
        url = generate_random_url()
        if not PaymentRecord.objects.filter(url=url).exists():
            return url
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user after registration
            login(request, user)
            return redirect('profile_view')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_view')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserProfileForm(request.POST)

            if form.is_valid():
                user_profile, created = UserProfile.objects.get_or_create(user=request.user)
                user_profile.first_name = form.cleaned_data['first_name']
                user_profile.last_name = form.cleaned_data['last_name']
                user_profile.paypal_email = form.cleaned_data['paypal_email']
                user_profile.save()

                # Generate a random URL for the payment record
                url = generate_random_url()
                user = request.user
                amount = form.cleaned_data.get('amount')
                if amount is not None:
                    record = PaymentRecord(user=user, amount=amount, url=url)
                    record.save()

                return redirect('payment_records_view', url=url)
            else:
                print("Form is invalid:", form.errors)

        else:
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            form = UserProfileForm(initial={'first_name': user_profile.first_name, 'last_name': user_profile.last_name, 'paypal_email': user_profile.paypal_email})
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('payment_records_view')

@login_required
def payment_records_view(request, url=None):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PaymentRecordForm(request.POST)
            if form.is_valid():
                user = request.user
                amount = form.cleaned_data['amount']
                url = generate_unique_url()  # Generate a new random URL if not provided
                record = PaymentRecord(user=user, amount=amount, url=url)
                record.save()
            return redirect('payment_records_view', url=url)
        else:
            form = PaymentRecordForm()

        payment_records = PaymentRecord.objects.filter(user=request.user)
        return render(request, 'payment_records.html', {'form': form, 'payment_records': payment_records, 'url': url})
    else:
        return redirect('login_view')
