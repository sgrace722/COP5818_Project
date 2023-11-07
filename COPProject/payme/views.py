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


def home(request):
	# users = Users.objects.all()
	# print(users)
	# return render(request, 'all_users.html', {'users': users})
	return render(request, 'index.html', {})


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
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
            generated_url = GenerateURL.objects.create(user=request.user, random_url=random_url, amount=amount, currency=currency)
            return redirect(reverse('payme:generate_url'))  # Redirect to the 'generate_url' view

    else:
        form = GenerateForm()
    return render(request, 'account/generate_url.html', {'form': form, 'user_links': user_links})



@login_required
def delete_link(request, pk):
    link = get_object_or_404(GenerateURL, pk=pk)
    if link.user == request.user:
        link.delete()
    return redirect('payme:generate_url')