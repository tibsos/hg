from django.db import models as m

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

class Player(m.Model):

    user = m.ForeignKey(User, on_delete = m.CASCADE)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:

        Player.objects.create(user = instance)
    