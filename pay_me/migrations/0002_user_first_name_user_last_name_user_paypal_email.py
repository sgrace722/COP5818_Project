# Generated by Django 4.2.5 on 2023-10-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='paypal_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
