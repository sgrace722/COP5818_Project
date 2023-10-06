from django.shortcuts import render, redirect
from django.contrib import messages
from payme_app.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['username'] = username
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'login.html')

def welcome(request):
    if 'username' in request.session:
        return render(request, 'welcome.html', {'username': request.session['username']})
    else:
        messages.error(request, 'You need to log in first.')
        return redirect('login')

def logout(request):
    request.session.pop('username', None)
    return redirect('login')
