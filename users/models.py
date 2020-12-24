from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), blank=False)
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    image = models.URLField(max_length=1023, null=True)
    description = models.CharField(max_length=2047, null=True)
    follower_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('view_artist', kwargs={'username': self.username})
