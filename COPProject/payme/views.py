from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import UserProfile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm
import secrets
import string
from .forms import GenerateForm
from .models import GenerateURL
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import requests
from decimal import Decimal

def home(request):
	# users = Users.objects.all()
	# print(users)
	# return render(request, 'all_users.html', {'users': users})
	return render(request, 'index.html', {})


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('payme:profile')

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'account/profile.html', {'form': form})





@login_required
def generate_url(request):
    user_links = GenerateURL.objects.filter(user=request.user)
    if request.method == 'POST':
        form = GenerateForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            currency = form.cleaned_data['currency']
            while True:
                random_url = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))
                if not GenerateURL.objects.filter(random_url=random_url).exists():
                    break
            
			# Calculate the equivalent value in USD
            # amount_usd = calculate_usd_equivalent(currency, amount)

            generated_url = GenerateURL.objects.create(user=request.user, random_url=random_url, amount=amount, currency=currency)
            return redirect(reverse('payme:generate_url'))  # Redirect to the 'generate_url' view
    else:
        form = GenerateForm()
        updated_user_links = []

        for link in user_links:
            # Calculate the equivalent value in USD for each row
            link.amount_usd = calculate_usd_equivalent(link.currency, link.amount)
            updated_user_links.append(link)

        return render(request, 'account/generate_url.html', {'form': form, 'user_links': updated_user_links})


@login_required
def delete_link(request, pk):
    link = get_object_or_404(GenerateURL, pk=pk)
    if link.user == request.user:
        link.delete()
    return redirect('payme:generate_url')


def process_url(request, random_url):
    # Look up the GenerateURL object based on the random_url
    generate_url = get_object_or_404(GenerateURL, random_url=random_url)

    # Construct the PayPal payment URL
    paypal_url = f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business={generate_url.user.userprofile.paypalemail}&amount={generate_url.amount}&currency_code={generate_url.currency}"

    # Redirect to the PayPal payment URL
    return HttpResponseRedirect(paypal_url)
    # return HttpResponse(f"Generated PayPal URL: <a href='{random_url}'>{random_url}</a>")

def calculate_usd_equivalent(currency, amount):
    print("calculate_usd_equivalent function is triggered")
    if currency == 'USD':
        return amount

    # Replace 'YOUR_API_KEY' with your actual API key from Free Currency API
    api_key = 'fca_live_KXdBZLfQrARvORwspxdSwiFC3SzOrnmR0eUMkoXT'  # Get your API key from https://app.freecurrencyapi.com

    # Make an API request to get the latest exchange rates
    api_url = f'https://api.freecurrencyapi.com/v1/latest'
    params = {'apikey': api_key}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data["data"][currency]  # Get the exchange rate for USD

        # Convert amount to Decimal and calculate the equivalent value in USD
        amount = Decimal(amount)
        amount_usd = amount / Decimal(exchange_rate)
        
		# Round the result to 2 decimal places
        # getcontext().prec = 3  # Set the precision (total number of significant digits)
        amount_usd = amount_usd.quantize(Decimal('0.00'), rounding='ROUND_DOWN')

        print(f"Result: {amount_usd}")
        return amount_usd
    else:
        # Unable to retrieve exchange rates, return the original amount or handle the error as needed
        print(f"Failed to get data.")
        return amount