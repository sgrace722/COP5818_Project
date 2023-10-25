from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm, ProfileForm
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                return HttpResponseRedirect(reverse('profile_view', args=[user.id]))
            except User.DoesNotExist:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def profile_view(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'profile.html', {'form': form, 'message': 'Profile updated successfully!'})
    else:
        form = ProfileForm(instance=user)

    return render(request, 'profile.html', {'form': form})

from django.shortcuts import redirect

def logout_view(request):
    return redirect('login_view')
