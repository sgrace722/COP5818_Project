from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import UserProfile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm


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
