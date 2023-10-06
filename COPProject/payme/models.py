from django.db import models
from django.contrib import auth
# Create your models here.

## UNSURE ABOUT model below, because we have not got that far in the chapters...
## But I will save it here for now LOL

# class LOGIN(models.Model):
#     user_name = models.CharField(
#         max_length=50, help_text="The users username to log into the site")
#     user_password = models.CharField(
#         max_length=50, help_text="The users password to log into the site")
#     user = models.ForeignKey(
#         auth.get_user_model(), on_delete=models.CASCADE)


class LOGIN(models.Model):
    user_name = models.CharField(
        max_length=50, help_text="The users username to log into the site", unique=True)
    user_password = models.CharField(
        max_length=50, help_text="The users password to log into the site")

