from django.shortcuts import render, redirect
from .forms import LoginForm, UrlForm
from .models import UserProfile


def home(request):
	# users = Users.objects.all()
	# print(users)
	# return render(request, 'all_users.html', {'users': users})
	return render(request, 'index.html', {})

def url_page(request):
    form = UrlForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dollar_amount = form.cleaned_data['dollar_amount']
            return render(request, 'link_page.html')
    return render(request, "url_page.html", {"form": form} )

# def login(request):
# 	if request.method == 'POST':
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password']

# 			# Debugging: Print or log the received form data
# 			print(f"Received username: {username}")
# 			print(f"Received password: {password}")
# 			users = Users.objects.all()
# 			print(users)
#             # Retrieve the user record from the database by username
# 			user = Users.objects.filter(username=username, password=password).first()

# 			if user:
# 				return render(request, 'welcome.html', {'username': username})
# 			else:
# 				# Display all contents of the user_credentials table for debugging
# 				all_users = Users.objects.all()
# 				return render(request, 'login.html', {'form': form, 'message': 'Incorrect credentials', 'all_users': all_users})

# 	else:
# 		form = LoginForm()

# 	return render(request, 'login.html', {'form': form})

# def all_users(request):
#     # Retrieve all user data from the Users model
#     users_data = Users.objects.values()

#     # Print the user data to the console (for debugging)
#     for user_data in users_data:
#         print(user_data)

#     # Render the 'all_users.html' template with the user data
#     return render(request, 'all_users.html', {'users_data': users_data})

# def all_users(request):
# 	users = Users.objects.all()
# 	print(users)
# 	return render(request, 'all_users.html', {'users': users})

