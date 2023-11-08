from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

	# Paypal Data
    paypalemail = models.EmailField(max_length=255, blank=True, null=True)

    # Additional fields here
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    # Add more fields as needed

    def __str__(self):
        return self.user.username



class GenerateURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    random_url = models.CharField(max_length=6, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

# Reminder:
# python -m pip install Pillow
# https://youtu.be/aOLrEkpGWDg?t=303
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser