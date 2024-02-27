from django.db import models as m

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save

class Player(m.Model):

    user = m.OneToOneField(User, on_delete = m.CASCADE, related_name = 'player')

    background = m.TextField(blank = True, null = True)

    def __str__(self):

        return self.user.username

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:

        Player.objects.create(user = instance)
    