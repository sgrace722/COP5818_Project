from django.db import models

class UserCredentials(models.Model):
	username = models.CharField(max_length=100, help_text="Enter your username")
	password = models.CharField(max_length=100, help_text="Enter your password")
	
	def __str__(self): return self.username