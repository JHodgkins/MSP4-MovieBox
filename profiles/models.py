"""
Import models so models can be refrenced.
Import User model so user details can be refrenced using the foreign key.
Import post_save to handle post requests passed through views.
Import receiver to handle reciever calls.
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Retrieves purchase history and any user delivery
    information, 1 to 1 relationship.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=40, null=True, blank=True, default='UK')
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creaton of a user profile section, if registered user
    details will be updated.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # for any logged in users, the profile will only be saved
    instance.userprofile.save()
