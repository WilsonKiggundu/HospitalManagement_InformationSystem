from django.contrib.auth.models import *
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, help_text='A brief description about the person you are adding '
                                                                 'to the system')
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True, help_text='Optional. Format: YYYY-MM-DD')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
