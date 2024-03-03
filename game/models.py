from django.db import models as m

from .utils import get_ip_country_city

class Event(m.Model):

    name = m.TextField()

    count = m.PositiveSmallIntegerField(default = 0)

    def __str__(self):

        return self.name