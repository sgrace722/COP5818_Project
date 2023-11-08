from django.contrib import admin
from .models import UserProfile
from .models import GenerateURL

admin.site.register(UserProfile)
admin.site.register(GenerateURL)